import sqlite3
import tkinter
import time
import PIL.Image, PIL.ImageTk
from PIL import Image,ImageTk
import cv2
import numpy as np
from tkinter import Tk, Label, Button, Entry, Toplevel

r=Tk()
conn = sqlite3.connect('imageset.db')
print("Opened database successfully");



def displayall():
    m,n=0,0
    t=Toplevel()
    cursor = conn.execute("""SELECT *
from A union all SELECT *
from B union all SELECT *                                    
from C union all SELECT *
from D union all SELECT *
from E union all SELECT *
from F union all SELECT *
from G union all SELECT *
from H union all SELECT *
from I union all SELECT *
from J union all SELECT *
from K union all SELECT *
from L union all SELECT *
from M union all SELECT *
from N union all SELECT *
from O union all SELECT *
from P union all SELECT *
from Q union all SELECT *
from R union all SELECT *
from S union all SELECT *
from T union all SELECT *
from U union all SELECT *
from V union all SELECT *
from W union all SELECT *
from X union all SELECT *
from Y union all SELECT *
from Z union all SELECT *
from user_6""")
    for row in cursor: 
        #print("ID = ", row[0])
        #print("img = ", row[1])
        blob_data=row[0]
        nparr  = np.frombuffer(blob_data, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        image1=cv2.resize(img_np,(130,100))
        #cv2.imshow("data",image1)
        #break
        #Rearrang the color channel
        b,g,r = cv2.split(image1)
        image1 = cv2.merge((r,g,b))
        # Convert the Image object into a TkPhoto object
        im = Image.fromarray(image1)
        imgtk = ImageTk.PhotoImage(image=im) 
        # Put it in the display window
        g=Label(t, image=imgtk)
        g.grid(row=m,column=n)
        g.image = imgtk
        m=m+1
        if(m>6):
            m=0
            n=n+1
    t.mainloop()
    conn.close()
            
def display():
    m,n=0,0
    c=str(en.get())
    print(c)
    t=Toplevel()
    d='%'+c+'%'
    sql = f"""SELECT * from (SELECT *
from A union all SELECT *
from B union all SELECT *
from C union all SELECT *
from D union all SELECT *
from E union all SELECT *
from F union all SELECT *
from G union all SELECT *
from H union all SELECT *
from I union all SELECT *
from J union all SELECT *
from K union all SELECT *
from L union all SELECT *
from M union all SELECT *
from N union all SELECT *
from O union all SELECT *
from P union all SELECT *
from Q union all SELECT *
from R union all SELECT *
from S union all SELECT *
from T union all SELECT *
from U union all SELECT *
from V union all SELECT *
from W union all SELECT *
from X union all SELECT *
from Y union all SELECT *
from Z union all SELECT *
from user_6) where Field2 like '%{d}%'"""
    cursor = conn.execute(sql)
    for row in cursor: 
        print("ID = ", row[1])
        #print("img = ", row[1])
        blob_data=row[0]
        nparr  = np.frombuffer(blob_data, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        image1=cv2.resize(img_np,(130,100))
        #cv2.imshow("data",image1)
        #break
        #Rearrang the color channel
        b,g,r = cv2.split(image1)
        image1 = cv2.merge((r,g,b))
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

    t.mainloop()
    conn.close()

def insert():
    print("insert")
    ins=en2.get()
     
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
             # Get a frame from the video source
            ret, frame = self.vid.get_frame()

            if ret:
                #cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
                imga=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img_str = cv2.imencode('.jpg', imga)[1].tostring()
                cursor=conn.execute("create table if not exists user_6 (Field1 blob, Field2 text)")
                cursor=conn.execute("insert into user_6 values (?,?)",(img_str,ins))
                conn.commit()

                

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
    App(tkinter.Toplevel(), "Tkinter and OpenCV")





def delete():
    print("delete")
    d=en3.get()
    print(d)
    cursor=conn.execute("delete from user_6 where Field2=?",(d,))
    conn.commit()

def DispA():
    m,n=0,0
    t=Toplevel()
    sql = f"""SELECT * from (SELECT *
from A union all SELECT *
from B union all SELECT *
from C union all SELECT *
from D union all SELECT *
from E union all SELECT *
from F union all SELECT *
from G union all SELECT *
from H union all SELECT *
from I union all SELECT *
from J union all SELECT *
from K union all SELECT *
from L union all SELECT *
from M union all SELECT *
from N union all SELECT *
from O union all SELECT *
from P union all SELECT *
from Q union all SELECT *
from R union all SELECT *
from S union all SELECT *
from T union all SELECT *
from U union all SELECT *
from V union all SELECT *
from W union all SELECT *
from X union all SELECT *
from Y union all SELECT *
from Z) where Field2 like '%0%'"""
    cursor = conn.execute(sql)
    for row in cursor: 
        #print("ID = ", row[1])
        #print("img = ", row[1])
        blob_data=row[0]
        nparr  = np.frombuffer(blob_data, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        image1=cv2.resize(img_np,(130,100))
        #cv2.imshow("data",image1)
        #break
        #Rearrang the color channel
        b,g,r = cv2.split(image1)
        image1 = cv2.merge((r,g,b))
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

    t.mainloop()
    conn.close()


def sen():
    print("")
    


r.title("GUI PL/DBMS")
Label(r,bg='pink',text="Enter alphabet to be displayed",font=("Arial", 15)).grid(row=0,pady=10)
en=Entry(r)
en.grid(row=1,padx=100,pady=10,ipadx=80,ipady=10)
b1=Button(r,text='DISPLAY',font=("Arial", 15),bg='white',command=display,width = 25)
b1.grid(row=2,pady=10)
b2=Button(r,text='DISPLAY ALL IMAGES',font=("Arial", 15),bg='white',command=displayall,width=25)
b2.grid(row=3)
Label(r,bg='pink',text="Enter data to be inserted",font=("Arial", 15)).grid(row=4,column=0,pady=10)
en2=Entry(r)
en2.grid(row=5,pady=10,ipadx=80,ipady=10)
b3=Button(r,text='INSERT',font=("Arial", 15),command=insert,bg='white',width=25)
b3.grid(row=6,pady=10)
en3=Entry(r)
en3.grid(row=8,padx=100,pady=10,ipadx=80,ipady=10)
Label(r,bg='pink',text="Enter data to be deleted",font=("Arial", 15)).grid(row=7,column=0,pady=10)
b5=Button(r,text='DELETE',font=("Arial", 15),bg='white',command=delete,width=25)
b5.grid(row=9,pady=10)
b6=Button(r,text='DISPLAY ALPHABETS',font=("Arial", 15),bg='white',command=DispA,width=25)
b6.grid(row=10,pady=10)
r.configure(bg='pink')
r.mainloop()


