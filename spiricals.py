import turtle
import os

from math import sin, cos, pi, ceil

def spiral_draw(a = 3, b = 5, delta = pi / 2, base_length = 100, origin = (0,0), step = 0.005):

    half_length = base_length / 2.0

    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    turtle.penup()

    x = origin[0] 
    y = origin[1] + half_length*sin(delta)

    turtle.goto((x,y))
    turtle.pendown()

    for t in range(1, int(ceil(2*pi/step))+1):
        x = origin[0] + half_length*sin(a*t*step)
        y = origin[1] + half_length*sin(b*t*step + delta)

        turtle.goto((x,y))


def composition_1(X = 9, Y = 5, base_length = 80):
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title("Spiral Curves")

    origin = (-X * 0.75 * base_length, Y * 0.75 * base_length)
    delta = pi / 2

    for x in range(X):
        for y in range(Y):
            o = (origin[0] + 1.5 * base_length * x, origin[1] - 1.5 * base_length * y)
            spiral_draw(x + 1, y + 1, delta, base_length, o)

    turtle.exitonclick()

def composition_2(X = 9, Y = 5, base_length = 80):
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    origin = (-X * 0.75 * base_length, Y * 0.75 * base_length)
    

    for x in range(X):
        for y in range(Y):
            o = (origin[0] + 1.5 * base_length * x, origin[1] - 1.5 * base_length * y)
            delta = pi * x / (X - 1)
            spiral_draw(1, y + 1, delta, base_length, o)

    turtle.exitonclick()

if __name__ == "__main__":
    composition_2()
