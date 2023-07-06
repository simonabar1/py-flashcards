from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# ------------ Generating Random Words and adding them to card
to_learn = {}
current_card = {}

try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    canvas.itemconfigure(card_word, text=current_card['French'], fill='black')
    canvas.itemconfigure(card_title, text='French', fill='black')
    canvas.itemconfigure(canvas_img, image=canvas_front_img)
    flip_timer = window.after(3000, func=flip_card)


# -------------- Define card flip --------

def flip_card():
    canvas.itemconfigure(canvas_img, image=canvas_back_img)
    canvas.itemconfigure(card_word, text=current_card['English'], fill='white')
    canvas.itemconfigure(card_title, text='English', fill='white')


# -------------- Define word removal --------
def is_known():
    to_learn.remove(current_card)
    new_data = pd.DataFrame(to_learn)
    new_data.to_csv('data/words_to_learn.csv', index=False)
    next_card()


# Window
window = Tk()
window.title('Flashcard')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)

# White Canvas for Flashcard
canvas = Canvas(width=800, height=526)
canvas_front_img = PhotoImage(file='images/card_front.png')
canvas_back_img = PhotoImage(file='images/card_back.png')
canvas_img = canvas.create_image(400, 263, image=canvas_front_img)
card_title = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, borderwidth=0, bd=0, command=is_known)
right_btn.grid(column=1, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, borderwidth=0, bd=0, command=next_card)
wrong_btn.grid(column=0, row=1)

# Call the next card
next_card()

# Keep window open
window.mainloop()
