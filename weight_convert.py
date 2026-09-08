from tkinter import *
import tkinter.font as font
root = Tk()
root.title("Weight Convertor")
root.geometry('500x100')

def convert():
    pass

frame = Frame(root)
frame.pack(pady=10)

enterlabel = Label(frame,text="Enter the weight in kg",font=font.Font(size=10))
enterlabel.grid(row=0,column=0)

enterentry = Entry(frame)
enterentry.grid(row=0,column=1)

submit = Button(frame,text="Convert",command=convert)
submit.grid(row=0,column=2)


gram = Label(frame,text="Gram",font=font.Font(size=10))
gram.grid(row=1,column=0)

gramlabel = Label(frame,font=font.Font(size=10))
gramlabel.grid(row=2,column=0)

pound = Label(frame,text="Pound",font=font.Font(size=10))
pound.grid(row=1,column=0)

poundlabel = Label(frame,font=font.Font(size=10))
poundlabel.grid(row=2,column=0)

ounce = Label(frame,text="Pound",font=font.Font(size=10))
ounce.grid(row=1,column=0)

ouncelabel = Label(frame,font=font.Font(size=10))
ouncelabel.grid(row=3,column=1)













root.mainloop()