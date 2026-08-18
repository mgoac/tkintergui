from tkinter import *
root = Tk()
root.geometry("800x800")
root.config(background='red')

Label(root,text="Email",width=11).place(x=250,y=70)
Entry(root).place(x=360,y=70)

Label(root,text="Password",width=11).place(x=250,y=100)
Entry(root).place(x=360,y=100)

Label(root,text="What food would you like: Chicken sandwich B.L.T, Veg Sandwich? or None",width=70).place(x=120,y=160)
Entry(root,width=25).place(x=150,y=200)
Spinbox(root,from_=0,to=10,width=25).place(x=440,y=200)

Label(root,text="What beverage would you like: Cola, Fanta, Orange juice, Water, or None?",width=70).place(x=120,y=300)
Entry(root,width=25).place(x=150,y=340)
Spinbox(root,from_=0,to=10,width=25).place(x=440,y=340)

Label(root,text="What dessert would you like: An Ice Cream, an Ice Lolly, or a Chocolate Cake or None?",width=70).place(x=120,y=440)
Entry(root,width=25).place(x=150,y=480)
Spinbox(root,from_=0,to=10,width=25).place(x=440,y=480)


Button(root,text="Submit Order",command=root.destroy).place(x=330,y=580)


root.mainloop()