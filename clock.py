import turtle

screen = turtle.Screen()
turtle = turtle.Turtle()

screen.setup(620, 620)
screen.bgcolor('black')

clr = ['red', 'green', 'blue', 'yellow', 'purple']

turtle.pensize(4)
turtle.shape('turtle')
turtle.penup()
turtle.pencolor('red')

m = 0

for i in range(12):
      m = m + 1

      turtle.penup()
      turtle.setheading(-30 * i + 60)
      turtle.forward(150)
      turtle.pendown()

      turtle.forward(25)
      turtle.penup()

      turtle.forward(20)
      turtle.write(str(m), align="center", font=("Arial", 12, "normal"))

      if m == 12:
        m = 0

      turtle.home()

turtle.home()
turtle.setpos(0, -250)
turtle.pendown()
turtle.pensize(10)

turtle.pencolor('blue')

turtle.circle(250)
turtle.penup()
turtle.setpos(150, -270)
turtle.pendown()

turtle.pencolor('olive')
turtle.write('Animation using Turtle!', font=("Arial", 12, "normal"))
turtle.ht()