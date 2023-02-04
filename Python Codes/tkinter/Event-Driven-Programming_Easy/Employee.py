from email.policy import default
from tkinter import *

from sqlalchemy import column
root=Tk()
Label(root,text="EmpID :").grid(row=0)
Label(root,text="Employee Name :").grid(row=1)
v1 = StringVar(root,"Manager")
Label(root,text="Job :").grid(row=2)
e1=Entry(root).grid(row=0,column=1)
e2=Entry(root).grid(row=1,column=1)
e3=Entry(root,textvariable=v1).grid(row=2,column=1)
Label(root,text="Employee Type").grid(row=3)
v = IntVar()
Radiobutton(root,text="Regular",variable=v,value=1).grid(row=3,column=1)
Radiobutton(root,text="Temporary",variable=v,value=2).grid(row=3,column=2)
Label(root,text="Salary").grid(row=4)
Spinbox(root,from_=5000,to=80000).grid(row=4,column=1)
Button(root,text="Insert").grid(row=5)
Button(root,text="Update").grid(row=5,column=1)
Button(root,text="Delete").grid(row=6)
Button(root,text="Select").grid(row=6,column=1)
mainloop()