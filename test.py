import turtle
from turtle import *
t = Turtle()
t.shape('turtle')

"""def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
square(200)
def equal(x):
    t.forward(x)
    t.left(120)
    t.forward(x)
    t.left(120)
    t.forward(x)
equal(200) 

def right():
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(135)
    t.forward(142)
right()

def rec(x):
    t.forward(x)
    t.left(90)
    t.forward(x+250)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x+250)
    t.left(90)
rec(200)

for i in range(3):
    print(i)"""
""""
for i in range(3):
    t.forward(1000)
    t.left(100)
    t.forward(500)
    t.right(50)"""
t.speed(10000)
t.shapesize(0.01)
screensize(10)
idelength = 100
rotate = 90
def square(x,y):
       for i in range(4):
        t.forward(x)
        t.left(y)
"""square(100,90)"""
"""def doubleSquares(iRange):
    length = 5
    for i in range(iRange):
        square(length, 90)
        length = length * 2
doubleSquares(5)"""
"""def addSquares(iRange):
    length = 100
    for i in range(iRange):
        square(length, 90)
        length += (0)
        t.left(-5)
addSquares(60)"""

"""def addSquares(iRange):
    length = 100
    for i in range(iRange):
        square(length, 90)
        length += (5)
        t.left(-5)
addSquares(60)"""
"""def star(iRange):
    length = 100
    for i in range(iRange):
        square(length, 90)
        length += (1)
        t.left(144)
star(60)"""

def sta(x,y):
       for i in range(3):
        t.forward(x)
        t.left(y)

def star(iRange):
    length = 100
    for i in range(iRange):
        sta(length, 122)
        length += (5)
        t.left(144)
star(600)