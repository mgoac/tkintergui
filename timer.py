from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("400x400")
root.title("Time Countdown")

timer = None

def stopset():
    global timer
    root.after_cancel(timer)

def runcountdown():
    global timer
    hours = int(n1.get())
    minutes = int(n2.get())
    seconds = int(n3.get())
    
    if seconds >= 60:
        minutes += seconds // 60
        seconds = seconds % 60


    if minutes >= 60:
        hours += minutes // 60
        minutes = minutes % 60
        
    if seconds == 0:
        if minutes == 0:
            if hours == 0:
                messagebox.showinfo("Timer","Time has ended.")
                return
            else:
                hours = hours - 1
                minutes = 59
                seconds = 59
        else:
            minutes = minutes - 1
            seconds = 59
    else:
        seconds -= 1

    n1.delete(0, END)
    n1.insert(0, str(hours))

    n2.delete(0, END)
    n2.insert(0, str(minutes))

    n3.delete(0, END)
    n3.insert(0, str(seconds))

    timer = root.after(1000, runcountdown)
    

        
    
n1 = Entry(root,width=3,font=("Arial",23))
n1.place(x=97,y=50)

n11 = Label(text=":")
n11.place(x=157,y=56)

n2 = Entry(root,width=3,font=("Arial",23))
n2.place(x=167,y=50)

n22 = Label(text=":")
n22.place(x=227,y=56)

n3 = Entry(root,width=3,font=("Arial",23))
n3.place(x=237,y=50)

errmsg = Label(root)
errmsg.place(x=117,y=200)

submit = Button(root,text="Set Time Countdown",command=runcountdown)
submit.place(x=117,y=150)

stop = Button(root,text="Stop Countdown",command=stopset)
stop.place(x=129,y=200)

root.mainloop()


"""
1. Firsst get the total countdown in seconds :
temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
2. check if the total countdown is more than 60, in that case, by using the divmod methos, you can get the tuple (quotient being the number of minutes and remainder being the number of left over seconds)
3. Now check the quotient, if the quotient, i.e. number of minutes is also more than or equal to 60 , we need a further conversion, for hours and minutes by using the divmod method again
4. Use the format method to show the values :
hour.set("{00:2d}".format(hours))
        minute.set("{00:2d}".format(mins))
        second.set("{00:2d}".format(secs))
6. The above is repeated in a loop till, the total reaches 0. Also in the loop, we use the time.sleep (1), which is the 1 second interval. also call the root.update() method to update the values of various widgets in the loop. 
7. In order to configure and change texts on the entry boxes for hour, minute and seconds, use the StringVar(). Example:
hour = StringVar()
hourEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=hour)
hour.set("{00:2d}".format(hours))
whenever the hour value changes, the widget display changes accordingly automatically."""