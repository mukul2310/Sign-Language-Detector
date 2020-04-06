
#download the image in download.png before running
from tkinter import *
from PIL import *
t=Tk()
def f():
    print("1")
def g():
    print("2")
def h():
    print("3")
def i():
    print("4")
def j():
    print("5")
img=PhotoImage(file="download.png")
Label(t,image=img).grid(row=0,column=3)
t.title("GUI PL/DBMS")
f1=Label(t,text="Entry",)
e1=Entry(t)
f1.grid(row=0,column=0,padx=100,pady=100)
e1.grid(row=0,column=1,padx=10,pady=10)
b1=Button(t,text="display",command=f)
b2=Button(t,text="Display all images",command=g)
b3=Button(t,text="Insert",command=h)
b4=Button(t,text="Update",command=i)
b5=Button(t,text="Delete",command=j)
b1.grid(row=1,column=0,padx=10,pady=10)
b2.grid(row=1,column=1,padx=10,pady=10)
b3.grid(row=2,column=0,padx=10,pady=10)
b4.grid(row=3,column=0,padx=10,pady=10)
b5.grid(row=4,column=0,padx=10,pady=10)
t.mainloop()
