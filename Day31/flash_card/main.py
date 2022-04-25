from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("MY FLASH CARD")
window.config(padx=50, pady=50)

canvas = Canvas(width=800, height=526)
my_image = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=my_image)
canvas.grid(column=0, row=0)

# button = Button(image=my_image, highlightthickness=0)

window.mainloop()

