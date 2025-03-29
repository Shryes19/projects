from tkinter import *
import pandas, random

BACKGROUND_COLOR = "#B1DDC6"
new_card = {}
to_learn = {}

try:
    data = pandas.read_csv("to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def to_print_red():
    global new_card,flip_timer
    window.after_cancel(flip_timer)
    new_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=new_card["French"])
    canvas.itemconfig(old_img, image = img1)
    flip_timer = window.after(3000, func=change_card)

def to_print_green():
    to_learn.remove(new_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("to_learn.csv",index=False)
    to_print_red()

def change_card():
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=new_card["English"])
    canvas.itemconfig(old_img, image=img2)


window = Tk()
window.title("flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=change_card)
canvas = Canvas(width=800, height=526, highlightthickness=0)

img1 = PhotoImage(file="card_front.png")
old_img = canvas.create_image(400, 263, image=img1)
img2 = PhotoImage(file="card_back.png")

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400,263,text="", font=("Areal", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

red_image = PhotoImage(file="wrong.png")
green_image = PhotoImage(file="right.png")
red_button = Button(image=red_image, highlightthickness=0, command=to_print_red)
red_button.grid(row=1, column=0)
green_button = Button(image=green_image, highlightthickness=0,command=to_print_green)
green_button.grid(row=1, column=1)

to_print_red()


window.mainloop()
