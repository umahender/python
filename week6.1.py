'''6.1 a. Write a function called draw_rectangle that takes a Canvas and a Rectangle as arguments and draws a
representation of the Rectangle on the Canvas.
'''
from tkinter import *


root = tk.Tk()

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
canvas.create_rectangle(10, 10, 100, 100, fill='blue')
root.mainloop()
