import tkinter as tk
from PIL import ImageTk
import winsound
import random

window = tk.Tk()

window.title("MP3")

window.geometry("1000x650")

giorno = ['gior giovvan.wav', 'golden experiensu.wav', 'MUDA.wav', 'WRYYYYY (1).wav']
bucci = ['ari ari ari ari.wav', 'arrivedercii.wav', 'edge.wav', 'GIORNO GIOVANNAH.wav']


# -----Sounds-----
def giogio():
    play = winsound.PlaySound(random.choice(giorno), winsound.SND_ALIAS | winsound.SND_ASYNC)


def bruno():
    play = winsound.PlaySound(random.choice(bucci), winsound.SND_ALIAS | winsound.SND_ASYNC)


# ---Background----
background_image = tk.PhotoImage("gieiwrf.png")
background_label = tk.Label(image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.image_names = background_image
# ----Title-----
title = tk.Label(text="JOJO'S BIZARRE QUOTES", font=("Comic Sans", 20))
title.grid(column=8, row=1)

# ----Buttons-----
button_image = ImageTk.PhotoImage(file='giornogiovanna.png')
button = tk.Button(image=button_image, height=300, width=292, command=giogio)
button.grid(column=2, row=2)

button_image2 = ImageTk.PhotoImage(file="brunobucciarati.png")
button2 = tk.Button(image=button_image2, height=300, width=292, command=bruno)
button2.grid(column=2, row=5)

window.mainloop()
