import turtle 

turtle.speed(5) 
  
for i in range(100): 
    turtle.circle(i * 5)
    turtle.circle(i * -5)
    turtle.left(i)
  
turtle.exitonclick()
