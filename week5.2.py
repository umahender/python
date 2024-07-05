#geometrical shapes and operations on them as its functions.

import math


def area_circle(radius):
    return math.pi*radius ** 2
    """Returns the area of a circle with the given radius"""
def area_rectangle(length, width):
    """Returns the area of a rectangle with the given length and width"""
    return length * width
def area_triangle(base, height):
    return 0.5*base*height
    """Returns the area of a triangle with the given base and height"""

def perimeter_circle(radius):
    return 2 * math.pi*radius
    """Returns the perimeter of a circle with the given radius"""
def perimeter_rectangle(length, width):
    """Returns the perimeter of a rectangle with the given length and width"""
    return 2 * (length+ width)
def perimeter_triangle(side1, side2, side3):
    """Returns the perimeter of a triangle with the given side lengths"""
    return side1 +side2 + side3


x=area_circle(10)
print(x)