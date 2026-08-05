from tkinter import *
root = Tk()
root.geometry("500x500")
root.config(background='pink')
usertxt = Label(root,text="Username",width=11).place(x=60,y=100)
userinp = Entry(root).place(x=170,y=100)

passtxt = Label(root,text="Password",width=11).place(x=60,y=130)
passinp = Entry(root,show="*").place(x=170,y=130)

submit = Button(root,text="Submit",background="green",command=root.destroy).place(x=210,y=170)
root.mainloop()