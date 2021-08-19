import random
from tkinter import *
import pandas
from random import choice
BACKGROUND_COLOR = "#B1DDC6"
word = {}
to_learn ={}
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def new_card():
    global word,flip_timer
    window.after_cancel(flip_timer)
    word = choice(to_learn)
    canva.itemconfig(card_title, text="French")
    canva.itemconfig(card_word, text=word["French"])
    flip_timer = window.after(3000,func=flip_card)

def flip_card():

    image2=PhotoImage(file="./images/card_back.png")
    canva.itemconfig(front_img, image=image2)
    canva.itemconfig(card_title, text="English", fill="white")
    canva.itemconfig(card_word, text=word["English"], fill="white")

def is_known():
    global to_learn
    to_learn.remove(word)
    data.to_csv("./data/words_to_learn.csv",index=False)

    new_card()


window = Tk()
window.title("Flash Card Project")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func=flip_card)
canva=Canvas(width=800,height=526)
image=PhotoImage(file="./images/card_front.png")
front_img = canva.create_image(400,263,image=image)
card_title = canva.create_text(400, 150, text="Title", font=("Calibre",40,"italic"))
card_word = canva.create_text(400, 263, text="Word", font=("Calibre",60,"bold"))
canva.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canva.grid(column=0,row=0, columnspan=2)
wrong_img = PhotoImage(file="./images/wrong.png")
right_img = PhotoImage(file="./images/right.png")
wrong = Button(image=wrong_img,highlightthickness=0,command=is_known)
wrong.config(bg = BACKGROUND_COLOR, highlightthickness=0)
right = Button(image=right_img,highlightthickness=0, command= new_card)
right.config(bg = BACKGROUND_COLOR, highlightthickness=0)
right.grid(column=0,row=1)
wrong.grid(column=1,row=1)
new_card()

window.mainloop()