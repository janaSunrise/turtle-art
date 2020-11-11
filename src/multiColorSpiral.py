import turtle
import math
import random
wn = turtle.Screen()
wn.bgcolor('black')
turtle1 = turtle.Turtle()
turtle1.speed(0)
turtle1.color('white')
rotate = int(360)


def drawCircles(t, size):
    for i in range(10):
        t.circle(size)
        size = size-4


def drawSpecial(t, size, repeat):
    for i in range(repeat):
        drawCircles(t, size)
        t.right(360/repeat)


drawSpecial(turtle1, 100, 10)
turtle2 = turtle.Turtle()
turtle2.speed(0)
turtle2.color('yellow')
rotate = int(90)


def drawCircles(t, size):
    for i in range(4):
        t.circle(size)
        size = size-10


def drawSpecial(t, size, repeat):
    for i in range(repeat):
        drawCircles(t, size)
        t.right(360/repeat)


drawSpecial(turtle2, 100, 10)
turtle3 = turtle.Turtle()
turtle3.speed(0)
turtle3.color('blue')
rotate = int(80)


def drawCircles(t, size):
    for i in range(4):
        t.circle(size)
        size = size-5


def drawSpecial(t, size, repeat):
    for i in range(repeat):
        drawCircles(t, size)
        t.right(360/repeat)


drawSpecial(turtle3, 100, 10)
turtle4 = turtle.Turtle()
turtle4.speed(0)
turtle4.color('orange')
rotate = int(90)


def drawCircles(t, size):
    for i in range(4):
        t.circle(size)
        size = size-19


def drawSpecial(t, size, repeat):
    for i in range(repeat):
        drawCircles(t, size)
        t.right(360/repeat)


drawSpecial(turtle4, 100, 10)
turtle4 = turtle.Turtle()
turtle4.speed(0)
turtle4.color('pink')
rotate = int(90)


def drawCircles(t, size):
    for i in range(4):
        t.circle(size)
        size = size-20


def drawSpecial(t, size, repeat):
    for i in range(repeat):
        drawCircles(t, size)
        t.right(360/repeat)


drawSpecial(turtle4, 100, 10)
wn.exitonclick()
