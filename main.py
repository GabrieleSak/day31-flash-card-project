import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Ariel", 40, "italic")
FONT_WORD = ("Ariel", 60, "bold")


def right_clicked():
    word = random.choice(words)
    word_fr = word["French"]
    canvas.itemconfig(title_text, text="French")
    canvas.itemconfig(word_text, text=word_fr)


def wrong_clicked():
    word = random.choice(words)
    word_fr = word["French"]
    canvas.itemconfig(title_text, text="French")
    canvas.itemconfig(word_text, text=word_fr)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 273, image=card_front_img)
title_text = canvas.create_text(400, 150, text="Title", fill="black", font=FONT_TITLE)
word_text = canvas.create_text(400, 263, text="Word", fill="black", font=FONT_WORD)
canvas.grid(column=0, row=0, columnspan=2)

right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, bg=BACKGROUND_COLOR, relief="flat", command=right_clicked)
right_button.grid(column=1, row=1)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, bg=BACKGROUND_COLOR, relief="flat", command=wrong_clicked)
wrong_button.grid(column=0, row=1)

words = pd.read_csv("data/french_words.csv").to_dict(orient="records")
print(type(words))

window.mainloop()
