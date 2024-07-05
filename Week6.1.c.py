from tkinter import *

from swampy.Gui import Point
from swampy.World import *


class Canvas:
    width = 500
    height = 500


class Point:
    x = 60
    y = 15


def draw_point(canvas, point):
    bbox = [[point.x, point.y], [point.x, point.y]]
    drawn_canvas = world.ca(canvas.width, canvas.height)
    drawn_canvas.rectangle(bbox, fill="black")


a_canvas = Canvas()
p = Point()
world = World()
draw_point(a_canvas, p)
world.mainloop()
