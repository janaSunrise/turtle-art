import turtle
import os


def fibonacci(order=18, base_length=3, origin=(-400, -200)):
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width=1.0, height=1.0)
    screen.title(name)

    # Basic turtle setup:
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    turtle.pendown()

    # Build instructions sequence:
    S, SS = "0", "01"
    for i in range(order):
        S, SS = SS, SS + S

    # Draw the curve:
    turtle.color("purple")
    for i, char in enumerate(S):
        turtle.forward(base_length)
        if char == "0":
            if i % 2:
                turtle.right(90)
            else:
                turtle.left(90)


if __name__ == "__main__":
    fibonacci()
