import turtle
import os


def snowflake(order=5, base_length=2, origin=(-300, 200)):
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width=1.0, height=1.0)
    screen.title("Snowflake")

    # Basic turtle setup:
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    turtle.pendown()

    # Build instructions sequence:
    seq = "F--F--F"
    for i in range(order):
        new_seq = ""
        for char in seq:
            if char == "F":
                new_seq += "F+F--F+F"
            else:
                new_seq += char
        seq = new_seq

    # Draw the curve:
    turtle.color("darkgoldenrod")
    for char in seq:
        if char == "F":
            turtle.forward(base_length)
        elif char == "+":
            turtle.left(60)
        elif char == "-":
            turtle.right(60)

    # Close the window:
    turtle.exitonclick()


if __name__ == "__main__":
    snowFlake()
