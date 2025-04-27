from tkinter import *
import pandas as pd
from random import randint, choice
import time

BACKGROUND_COLOR = "#B1DDC6"
timer=None
SECONDS = 3

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = choice(to_learn)
    titles =list(current_card.keys())
    # Code written to be more general not just be for french flash cards
    front_title = titles[0]
    canvas.itemconfig(card_image, image=card_front_img)
    canvas.itemconfig(card_title, text=front_title)
    canvas.itemconfig(card_content, text=current_card[front_title])

    timer = window.after(SECONDS*1000, func=flip_card)


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def flip_card():
    global current_card
    back_title = list(current_card.keys())[1]
    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(card_title, text=back_title)
    canvas.itemconfig(card_content, text=current_card[back_title])



# ------------------------------------ User Interface -------------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 24, "italic"))
card_content = canvas.create_text(400, 263, text="Date", font=("Ariel", 30, "bold"))
next_card()
canvas.grid(row=0, column=0, columnspan=2)


#Buttons
check_mark_image = PhotoImage(file="images/right.png")
correct_button = Button(image=check_mark_image, borderwidth=0, highlightthickness=0, command=next_card)
correct_button.grid(row=1, column=0)

x_mark_image = PhotoImage(file="images/wrong.png")
incorrect_button = Button(image=x_mark_image, borderwidth=0, highlightthickness=0, command=is_known)
incorrect_button.grid(row=1, column=1)

window.mainloop()