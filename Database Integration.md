# Sign-Language-Detector
import sqlite3
from PIL import Image
import cv2
import numpy as np


image = Image.open(r"C:\Users\ABC\Desktop\Python tut\Dataset\user_3\A0.jpg")

def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.show(data)

conn = sqlite3.connect('datastorage.db')
print("Opened database successfully");


cursor = conn.execute("SELECT * from user_2")
for row in cursor:
   print("ID = ", row[0])
   print("img = ", row[1])
   blob_data=row[1]
   nparr  = np.frombuffer(blob_data, np.uint8)
   img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
   image=cv2.resize(img_np,(130,100))
   cv2.imshow("data",image)


print("Operation done successfully");
conn.close()
