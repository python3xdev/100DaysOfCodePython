# https://github.com/hermitdave/FrequencyWords/tree/master/content/2018

import pandas
from tkinter import *
from random import choice
BACKGROUND_COLOR = "#B1DDC6"
TIME = 3  # seconds
current_card = {}
to_learn = {}
language_file = "ukrainian_words"

# ------------------------ READING THE CSV FILE ------------------------ #

try:
    data_frame = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data_frame = pandas.read_csv(f"data/{language_file}.csv")

to_learn = data_frame.to_dict(orient='records')

LEARNING_LANGUAGE = pandas.read_csv(f"data/{language_file}.csv").columns[0]
KNOWN_LANGUAGE = pandas.read_csv(f"data/{language_file}.csv").columns[1]

# ------------------------ FUNCTIONS ------------------------ #


def flip_card():
    global current_card
    next_word = current_card[KNOWN_LANGUAGE]
    canvas.itemconfig(flash_card_img, image=card_back_img)
    canvas.itemconfig(language_label, text=KNOWN_LANGUAGE, fill="white")
    canvas.itemconfig(word_label, text=next_word, fill="white")


def next_card():
    global timer, current_card
    window.after_cancel(timer)
    current_card = choice(to_learn)
    next_word = current_card[LEARNING_LANGUAGE]
    canvas.itemconfig(flash_card_img, image=card_front_img)
    canvas.itemconfig(language_label, text=LEARNING_LANGUAGE, fill="black")
    canvas.itemconfig(word_label, text=next_word, fill="black")
    timer = window.after(3000, flip_card)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()

# ------------------------ UI ------------------------ #


window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

timer = window.after(3000, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
# We are adding them to variables so we can edit them later...
flash_card_img = canvas.create_image(400, 263, image=card_front_img)
language_label = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_label = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

# Buttons
cross_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

check_mark_img = PhotoImage(file="images/right.png")
right_button = Button(image=check_mark_img, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

next_card()  # We run this so that we can change the contents of the labels...

window.mainloop()
