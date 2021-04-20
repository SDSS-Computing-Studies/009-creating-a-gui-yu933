#This imports the tkinter file as tk
import tkinter as tk 

#This imports all the functions associated with the tkintter file as if they were in your local file
from tkinter import *

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")


label1 = tk.Label(window,text="Client Database")

dogphoto = PhotoImage(file="dog.png")
label2 = tk.Label(window, image=dogphoto)

label31 = tk.Label(window, text="Name")
label32 = tk.Label(window, text="Type")
label33 = tk.Label(window, text="Breed")
label34 = tk.Label(window, text="Owner")
label35 = tk.Label(window, text="Birthdate")

entry1 = tk.Entry(window,text="Entry widgets can be typed in", width=10)
entry2 = tk.Entry(window,text="Entry widgets can be typed in", width=10)
entry3 = tk.Entry(window,text="Entry widgets can be typed in", width=10)
entry4 = tk.Entry(window,text="Entry widgets can be typed in", width=10)
entry5 = tk.Entry(window,text="Entry widgets can be typed in", width=10)

button1 = tk.Button(window,text="Search by Name")
button2 = tk.Button(window,text="<Previous")
button3 = tk.Button(window,text="Next>")

button4 = tk.Button(window,text="Save Entry")

entry6 = tk.Entry(window,text="Entry widgets can be typed in")

button1.grid(row = 1, column = 3)
entry6.grid(row = 1, column = 4, columnspan = 2)
label2.grid(row = 1, column = 1, rowspan = 2)
label1.grid(row = 2, column = 3)

label31.grid(row = 3, column = 1)
label32.grid(row = 3, column = 2)
label33.grid(row = 3, column = 3)
label34.grid(row = 3, column = 4)
label35.grid(row = 3, column = 5)

entry1.grid(row = 4, column = 1)
entry2.grid(row = 4, column = 2)
entry3.grid(row = 4, column = 3)
entry4.grid(row = 4, column = 4)
entry5.grid(row = 4, column = 5)

button2.grid(row = 5, column = 1)
button3.grid(row = 5, column = 5)
button4.grid(row = 5, column = 3)

window.mainloop()