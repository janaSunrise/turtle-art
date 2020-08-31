import turtle
import os


def square(order=7, base_length=5, origin=(-350, -300)):
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
    seq = "a"
    for i in range(order):
        new_seq = ""
        for char in seq:
            if char == "a":
                new_seq += "-bF+aFa+Fb-"
            elif char == "b":
                new_seq += "+aF-bFb-Fa+"
            else:
                new_seq += char
        seq = new_seq

    # Draw the curve:
    turtle.color("dodgerblue")
    for char in seq:
        if char == "F":
            turtle.forward(base_length)
        elif char == "+":
            turtle.right(90)
        elif char == "-":
            turtle.left(90)

    # Close the window:
    turtle.exitonclick()


if __name__ == "__main__":
    square()
