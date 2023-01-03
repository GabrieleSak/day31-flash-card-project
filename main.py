import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Ariel", 40, "italic")
FONT_WORD = ("Ariel", 60, "bold")

try:
    words = pandas.read_csv("data/words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    words = pandas.read_csv("data/french_words.csv").to_dict(orient="records")

word = {}


def next_card():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(words)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=word["French"], fill="black")
    canvas.itemconfig(card_img, image=card_front_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(word_text, text=word["English"])
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(title_text, fill="white")
    canvas.itemconfig(word_text, fill="white")


def known_word():
    global words, word
    words.remove(word)

    pandas.DataFrame(words).to_csv("data/words_to_learn.csv", index=False)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 273, image=card_front_img)
title_text = canvas.create_text(400, 150, text="Title", fill="black", font=FONT_TITLE)
word_text = canvas.create_text(400, 263, text="Word", fill="black", font=FONT_WORD)
canvas.grid(column=0, row=0, columnspan=2)

right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, bg=BACKGROUND_COLOR, relief="flat",
                      command=lambda: [known_word(), next_card()])
right_button.grid(column=1, row=1)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, bg=BACKGROUND_COLOR, relief="flat", command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()
