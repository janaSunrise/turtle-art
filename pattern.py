import turtle
import os


def pattern(order=3, base_length=5, origin=(100, 200)):
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width=1.0, height=1.0)
    screen.title("A Simple Pattern")

    # Basic turtle setup:
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    turtle.left(180)
    turtle.pendown()

    # Build instructions sequence:
    seq = "F-F-F-F"
    for i in range(order):
        new_seq = ""
        for char in seq:
            if char == "F":
                new_seq += "F+F-F-FF+F+F-F"
            else:
                new_seq += char
        seq = new_seq

    # Draw the curve:
    turtle.color("crimson")
    for char in seq:
        if char == "+":
            turtle.right(90)
        elif char == "-":
            turtle.left(90)
        else:
            turtle.forward(base_length)

    # Close the window:
    turtle.exitonclick()


if __name__ == "__main__":
    pattern()
