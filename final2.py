import tkinter
import time
import math
import numpy as np

import imagehash


import PIL.Image, PIL.ImageTk
import sqlite3
from PIL import Image,ImageTk
import cv2
from tkinter import Tk, Label
#t=Tk()

conn = sqlite3.connect('datastorage.db')
print("Opened database successfully");
m,n=0,0

hash_arr=[]
id_arr=[]
min_id=[]



 
class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source

         # open video source (by default this will try to open the computer webcam)
        self.vid = MyVideoCapture(self.video_source)

         # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()

         # Button that lets the user take a snapshot
        self.btn_snapshot=tkinter.Button(window, text="Snapshot", width=50, command=self.snapshot)
        self.btn_snapshot.pack(anchor=tkinter.CENTER, expand=True)

         # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        self.update()

        self.window.mainloop()

    def snapshot(self):
        global hash_arr,id_arr,min_id,diff_arr,diff_id_arr,diff_min_id
         # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            #cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            hsv=cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
            kernel = np.ones((3,3),np.uint8)
            #cv2.imshow('hsv',hsv)
            lower_skin = np.array([0,20,70], dtype=np.uint8)
            upper_skin = np.array([20,255,255], dtype=np.uint8)
            mask = cv2.inRange(hsv, lower_skin, upper_skin)
            mask = cv2.dilate(mask,kernel,iterations = 4)
            mask = cv2.GaussianBlur(mask,(5,5),100)
            mask1=cv2.resize(mask,(260,200))
            cv2.imshow('mask',mask1)
            #cv2.imshow('frame',frame)


            cursor = conn.execute("""SELECT * from user_1 union all SELECT *
            from user_3 union all SELECT *
            from user_4 union all SELECT *
            from user_5 union all SELECT *
            from user_2""")
            for row in cursor: 
                #print("ID = ", row[0])


                #print("img = ", row[1])
                blob_data=row[1]
                nparr  = np.frombuffer(blob_data, np.uint8)
                img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                image1=cv2.resize(img_np,(260,200))
                #cv2.imshow("data",image1)
                #break
                #Rearrang the color channel
                b,g,r = cv2.split(image1)
                image1 = cv2.merge((r,g,b))
                hsv1=cv2.cvtColor(image1, cv2.COLOR_RGB2HSV)
                kernel2 = np.ones((3,3),np.uint8)
                lower_skin = np.array([0,20,70], dtype=np.uint8)
                upper_skin = np.array([20,255,255], dtype=np.uint8)
                mask2 = cv2.inRange(hsv1, lower_skin, upper_skin)
                mask2 = cv2.dilate(mask2,kernel2,iterations = 4)
                mask2 = cv2.GaussianBlur(mask2,(5,5),100)
                mask2=cv2.resize(mask2,(260,200))
                #cv2.imshow('mask',mask2)
                #break
                '''
                # Convert the Image object into a TkPhoto object
                im = Image.fromarray(image1)
                imgtk = ImageTk.PhotoImage(image=im)
                
                # Put it in the display window
                g=Label(t, image=imgtk)
                g.grid(row=m,column=n)
                g.image = imgtk
                m=m+1
                if(m>4):
                    m=0
                    n=n+1

            '''
                

                hash = imagehash.phash(Image.fromarray(mask1))
                otherhash = imagehash.phash(Image.fromarray(mask2))

                hash_arr.append(hash - otherhash)
                id_arr.append(row[0][0])
                
            print("hash_arr",hash_arr)
            min_diff=min(hash_arr)
            
            print(min_diff)
            def most_frequent(List): 
                counter = 0
                num = List[0] 
                  
                for i in List: 
                    curr_frequency = List.count(i) 
                    if(curr_frequency> counter): 
                        counter = curr_frequency 
                        num = i 
              
                return num
            for i in range(len(hash_arr)):
                if(hash_arr[i]==min_diff):
                    min_id.append(id_arr[i])
                
            
            print(min_id)
            print(most_frequent(min_id))
        
            hash_arr=[]
            min_id=[]
            id_arr=[]
##            cursor = conn.execute("""SELECT id from
##            (select id from user_1 union all SELECT id
##            from user_3 union all SELECT id
##            from user_4 union all SELECT id
##            from user_5 union all SELECT id
##            from user_2) where id=?""",min_id)
    
  

                

    def update(self):
         # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
             self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
             self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)

        self.window.after(self.delay, self.update)


class MyVideoCapture:
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

         # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                 # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

     # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

    # Create a window and pass it to the Application object
App(tkinter.Tk(), "Tkinter and OpenCV")










cv2.destroyAllWindows()
#capture.release()    







print("Operation done successfully");
conn.close()
