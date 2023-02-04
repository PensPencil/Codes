import tkinter as tk
root = tk.Tk()
root.title('First Try')
button = tk.Button(root,text = 'Bye Now !!!',command=root.destroy,activeforeground='Blue')
button.pack()
root.mainloop()