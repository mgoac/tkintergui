import tkinter as tk

window = tk.Tk()
window.title("Traffic Light")
window.geometry("300x300")

red_button = tk.Button(window, text="STOP", bg="red", fg="white")
green_button = tk.Button(window, text="GO", bg="green", fg="white")
yellow_button = tk.Button(window, text="WAIT", bg="yellow", fg="black")

red_button.place(x=120, y=20)
green_button.place(x=120, y=250)
yellow_button.place(x=20, y=120)

window.mainloop()