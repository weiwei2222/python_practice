from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=50, pady=50)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

text_miles = Label(text="Miles")
text_miles.grid(column=2, row=0)

is_equal = Button(text="is equal")
is_equal.grid(column=0, row=1)

calculate_km = Label(text="0")
calculate_km.grid(column=1, row=1)

text_km = Label(text="Km")
text_km.grid(column=2, row=1)


def button_clicked():
    miles = float(miles_input.get())
    km = round(miles * 1.6)
    calculate_km.config(text=km)


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)











window.mainloop()