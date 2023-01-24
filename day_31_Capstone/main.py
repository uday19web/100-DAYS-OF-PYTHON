import random
from tkinter import *

import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    # read the csv data
    word_data = pandas.read_csv("./data/words_to_learn.csv.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    # print(type(word_data))
    to_learn = word_data.to_dict(orient="records")


# ----------------------------button functions-------------
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # itemconfig to used to update the existing one in the canvas
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=front_logo)
    flip_timer = window.after(3000, func=flip_word)


def flip_word():
    global current_card
    english_word = current_card["English"]
    canvas.itemconfig(canvas_image, image=back_logo)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=english_word, fill="white")


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


# ---------------------UI_-------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_word)
# canvas with front image
canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
front_logo = PhotoImage(file="./images/card_front.png")
back_logo = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_logo)
canvas.grid(row=0, column=0, columnspan=2)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

# buttons
right_logo = PhotoImage(file="./images/right.png")
right_button = Button(image=right_logo, command=is_known, highlightthickness=0)
right_button.grid(row=1, column=1)

wrong_logo = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_logo, command=next_card, highlightthickness=0)
wrong_button.grid(row=1, column=0)

# why we called here means it will show the french without showing the title and words in defualt we mentioned
next_card()

window.mainloop()
