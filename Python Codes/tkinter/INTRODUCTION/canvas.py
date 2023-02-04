from tkinter import *
master = Tk()
master.title("Sample Line")
master.geometry("600x600")
w = Canvas(master, width=600, height=400,bg='Black')
w.place(relx=0.5,rely=0.5,anchor=CENTER)
canvas_height=20
canvas_width=200
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y,fill='White')
button = Button(master,width=100,text='Close Window',command=master.destroy,activeforeground='White',bg='Black',fg='White')
button.pack(side=BOTTOM)
mainloop()