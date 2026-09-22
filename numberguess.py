from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.geometry("400x400")

frame = Frame(root)
frame.pack()

def checkguess():
    winner = random.randint(1,20)
    displayname = entry.get()
    theguess = entry1.get()
    if theguess:
        theguess = int(theguess)
    else:
        pass

    if displayname:
        if not theguess:
            messagebox.showinfo("Welcome",f"Well,{displayname}, I'm thinking of a number between 1-20 so guess!")
        else:
            if winner == theguess:
                winmsg.config(text="You won! That was the right number!")
            else:
                winmsg.config(text=f"Nope. The number was {winner}")
    else:
        messagebox.showerror("Invalid Input","Please Enter your name (and guess)")
    



name = Label(frame,text="Enter your name: ")
name.grid(row=0,column=0)

entry = Entry(frame)
entry.grid(row=0,column=1)

guess = Label(frame,text="Guess a number 1-20: ")
guess.grid(row=1,column=0)

entry1 = Entry(frame)
entry1.grid(row=1,column=1)

submit = Button(frame,text="Guess now!",command = checkguess)
submit.grid(row=4,column=1)

winmsg = Label(frame,text="")
winmsg.grid(row=6,column=1)

root.mainloop()