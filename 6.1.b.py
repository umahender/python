#b. Add an attribute named color to your Rectangle objects and modify draw rectangle so that ituses the color attribute as the fill color
import tkinter as tk
from tkinter import *
#Create an instance of tkinter frame
win= Tk()

#Define the geometry of window
win.geometry("600x400")
#Create a canvas object
c= tk.Canvas(win,width=400, height=400)
c.pack()
#Draw an Circle  in the canvas
c.create_oval(60, 60, 210, 210,fill="orange")

win.mainloop()