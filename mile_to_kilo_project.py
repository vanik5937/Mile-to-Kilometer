from tkinter import *

window = Tk()
window.title("Miles to Kilometer")
#window.minsize(width=200, height=200)
window.config(padx=30, pady= 30)

miles_input = Entry(width=8)
miles_input.grid(column = 1, row =0)

miles_label = Label(text = "Miles")
miles_label.grid(column = 2, row =0)

label = Label(text = "is equal to ")
label.grid(row =1, column = 0)
km_label = Label(text = "0")
km_label.grid(column =1, row=1)

km2_label = Label(text = "km")
km2_label.grid(column = 2, row =1)

def calc():
   km = float(miles_input.get()) * 1.6
   km_label.config(text = f"{km}")

button = Button(text="Calculate", command = calc)
button.grid(row = 2, column=1)


window.mainloop()




