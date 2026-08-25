from tkinter import *
root = Tk()
root.geometry("400x300")
root.title("Calendar")

title = Label(root,text="CALENDAR",fg="red",font=("Arial", 24, "bold"))
title.pack(side=TOP)

intro = Label(root,text="Enter any year below:",fg="green",font=("Courier", 12, "bold"))
intro.place(x=95,y=50)
year = Entry(root,width=26).place(x=95,y=70)

mainloop()