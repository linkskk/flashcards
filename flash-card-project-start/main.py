from tkinter import *

import pandas
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
# Select random French word

try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv('data/french_words.csv')
finally:
    french_data = data.to_dict(orient='records')

def select_french_word():
    global flip_timer, current_card
    window.after_cancel(flip_timer)
    current_card = choice(french_data)
    canvas.itemconfig(title, text="French", fill = 'black')
    canvas.itemconfig(french_word, text= f"{current_card['French']}", fill = 'black')
    canvas.itemconfig(flashy, image=card_front)
    flip_timer = window.after(10000, func = translate_french)

def word_correct():
    french_data.remove(current_card)
    data = pandas.DataFrame(french_data)
    data.to_csv("data/words_to_learn.csv", index=False)
    select_french_word()

# Translate French word:
def translate_french():
    canvas.itemconfig(title, text="English", fill='white')
    canvas.itemconfig(french_word, text= f"{current_card['English']}", fill = 'white')
    canvas.itemconfig(flashy, image=card_back)


flip_timer = window.after(3000, func = translate_french)

# UI SETUP

window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
flashy = canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR)

# card labels
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
french_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

check_mark = PhotoImage(file="images/right.png")
button = Button(image=check_mark, highlightthickness=0, command=word_correct)
button.grid(row=1, column=0)

cross = PhotoImage(file="images/wrong.png")
button = Button(image=cross, highlightthickness=0, command=select_french_word)
button.grid(row=1, column=1)

select_french_word()

#flip card

window.mainloop()
