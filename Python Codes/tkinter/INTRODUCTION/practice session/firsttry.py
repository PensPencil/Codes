from tkinter import *
root=Tk()
root.geometry("400x400")
Label(root,text="Regno :").grid(row=0,column=0)
Label(root,text="Name :").grid(row=1,column=0)
Label(root,text="Dept :").grid(row=2,column=0)
e1=Entry(root).grid(row=0,column=1)
e2=Entry(root).grid(row=1,column=1)
s=StringVar()
s.set("CSE")
e3=Entry(root,textvariable=s).grid(row=2,column=1)
v=IntVar()
Label(root,text="Gender").grid(row=3)
Radiobutton(root,variable=v,value=1).grid(row=3,column=1)
Radiobutton(root,variable=v,value=2).grid(row=3,column=2)
Label(root,text="Age").grid(row=4)
Spinbox(root,from_=18,to=100).grid(row=4,column=1)
Button(root,text="Insert").grid(row=5,column=0)
Button(root,text="Update").grid(row=5,column=1)
Button(root,text="Delete").grid(row=6,column=0)
Button(root,text="Select").grid(row=6,column=1)
mainloop()