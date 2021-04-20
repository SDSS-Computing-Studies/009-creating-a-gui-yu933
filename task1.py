#This imports the tkinter file as tk
import tkinter as tk 

#This imports all the functions associated with the tkintter file as if they were in your local file
from tkinter import *

window = tk.Tk()
window.title("tk")
entry1 = tk.Entry(window,text="Entry widgets can be typed in", width=10)
entry2 = tk.Entry(window,text="Entry widgets can be typed in", width=10)
entry3 = tk.Entry(window,text="Entry widgets can be typed in", width=10)

label1 = tk.Label(window,text="x")
label2 = tk.Label(window,text="=")
'''
entry1.pack()
entry2.pack()
entry3.pack()

label1.pack()
label2.pack()
'''
entry1.grid(row = 1, column = 1)
label1.grid(row = 1, column = 2)
entry2.grid(row = 1, column = 3)
label2.grid(row = 1, column = 4)
entry3.grid(row = 1, column = 5)



window.mainloop()