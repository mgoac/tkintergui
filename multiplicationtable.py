from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Mathematical table")

title = Label(window,text="Mathematical Table")

caption = Label(window,text="Number and Range:")

title.grid(row=0, column=0, columnspan=3,pady=25)
caption.grid(column=0, row=1, padx=10)

theNum = IntVar()
numbers = Combobox(window, textvariable=theNum, width=5)

numbers['values'] = tuple(range(11))

endVal =IntVar()
x10 = Radiobutton(window,text="10", variable=endVal, value=10)
x10 = Radiobutton(window,text="20", variable=endVal, value=20)
x10 = Radiobutton(window,text="30", variable=endVal, value=30)






















































































window.mainloop()