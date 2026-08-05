from tkinter import *
root = Tk()
root.geometry("400x400")
button = Button(root,bd=5,text="Click me!",background='red',command=root.destroy)
button.pack(side='right')
root.mainloop()