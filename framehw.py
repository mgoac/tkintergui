from tkinter import *
root = Tk()
root.geometry("400x400")
root.title("Control Panel")

topframe = Frame(root)
topframe.pack()

bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

start = Button(topframe,text="Start",fg="green")
stop = Button(topframe,text="Stop",fg="red")
start.pack(side=LEFT)
stop.pack(side=RIGHT)

settings = Button(bottomframe,text="Settings",fg="black")
exitb = Button(bottomframe,text="Exit",fg="red")
settings.pack(side=LEFT)
exitb.pack(side=RIGHT)

root.mainloop()