#This imports the tkinter file as tk
import tkinter as tk 

#This imports all the functions associated with the tkintter file as if they were in your local file
from tkinter import *

window = tk.Tk()
window.title("Example")

dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)

label2 = tk.Label(window,text="Pochacco!")

label3 = tk.Label(window, text=
"A cuddly little puppy! This is from the same \n creators who brought you Keropi and Kero Kero", bg = "#33FFFF")

label1.grid(row = 1, column = 2, rowspan = 3)
label2.grid(row = 2, column = 3)
label3.grid(row = 4, column = 1, columnspan = 5)

window.mainloop()