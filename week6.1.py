'''6.1 a. Write a function called draw_rectangle that takes a Canvas and a Rectangle as arguments and draws a
representation of the Rectangle on the Canvas.
'''
from tkinter import *

from matplotlib.patches import Rectangle


class Canvas(object):
        a_canvas = Canvas()
        a_canvas.width = 500
        a_canvas.height = 500

class Rectangle(object):
       p=Canvas()
       box = p.create_Rectangle() box.color = 'orange'
       box.bbox = [[-100, -60],[100, 60]]
def draw_rectangle(canvas, rectangle):
    drawn_canvas = world.ca(canvas.width, canvas.height)
    drawn_canvas.rectangle(rectangle.bbox, fill=rectangle.color)
    world = World()


draw_rectangle(a_canvas, box)
world.mainloop()
