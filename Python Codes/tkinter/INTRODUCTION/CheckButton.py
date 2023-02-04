from tkinter import *
root = Tk()
root.geometry("50x50")
var1=IntVar()
Checkbutton(root,text='Male',variable=var1).grid(row=0,sticky=W)
var2=IntVar()
Checkbutton(root,text='Female',variable=var2).grid(row=1,sticky=W)
mainloop()