from tkinter import *

OPTIONS = [
"Jan",
"Feb",
"Mar"
] #etc

master = Tk()

variable = StringVar(master,"Month")
 # default value

w = OptionMenu(master, variable, *OPTIONS)
w.pack()

mainloop()