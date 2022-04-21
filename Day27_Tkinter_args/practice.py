from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

my_label = Label(text="I like 🐱", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)
# my_label["text"] = "new text"


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="new click me")
new_button.grid(column=2, row=0)

input = Entry(width=10)
input.grid(column=3, row=2)







window.mainloop()