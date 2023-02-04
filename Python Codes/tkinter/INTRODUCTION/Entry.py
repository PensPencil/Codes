from tkinter import *
root =Tk()
root.title("No Entry")
Label(root,text='First Name :').grid(row=0)
Label(root,text='Last Name :').grid(row=1)
e1=Entry(root).grid(row=0,column=1)
e2=Entry(root).grid(row=1,column=1)

mainloop()