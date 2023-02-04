from cProfile import label
from tkinter import *
master = Tk()
master.title('Slowpoke')
master.geometry("600x600")
w=Label(master,text='I am a pokemon !!!',bg='green')
w.pack()
mainloop()