from tkinter import *
import calendar

def showCal():
    new_gui = Tk()
    new_gui.config(background="white")
    new_gui.title("CALENDAR")
    new_gui.geometry("700x650")
    fetch_year = int(year.get())
    cal_content = calendar.calendar(fetch_year)
    cal_year = Label(new_gui,text=cal_content,font="Consolas 10 bold")

    cal_year.grid(row=5,column=1,padx=20)

    new_gui.mainloop()
root = Tk()
root.geometry("220x205")
root.title("Calendar")

title = Label(root,text="CALENDAR",fg="red",font=("Arial", 24, "bold"))
title.pack(side=TOP)

intro = Label(root,text="Enter any year below:",fg="green",font=("Courier", 12, "bold"))

year = Entry(root,width=26)

Show = Button(root,text="Show Calendar",fg="black",bg="red",command=showCal)
Exit = Button(root,text="Exit",fg="black",bg="red",command=root.destroy)

title.grid(row=1,column=1)

intro.grid(row=2,column=1)

year.grid(row=3,column=1)

Show.grid(row=4,column=1)

Exit.grid(row=6,column=1)

mainloop()