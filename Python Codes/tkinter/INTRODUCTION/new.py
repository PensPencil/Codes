from tkinter import *

def choice():

    if(radio.get()==1):
        root.configure(background='red')
    elif(radio.get()==2):
        root.configure(background='blue')
    elif(radio.get()==3):
        root.configure(background='green')

root= Tk()
root.geometry("1000x1000")
radio=IntVar()
rb1=Radiobutton(root,text='Red', variable=radio,width=50,value=1, command=choice)
rb1.grid(row=0)
rb2=Radiobutton(root,text='Blue', variable=radio,width=50,value=2, command=choice)
rb2.grid(row=1)
rb3=Radiobutton(root,text='Green', variable=radio,width=50,value=3, command=choice)
rb3.grid(row=3)
root.mainloop()