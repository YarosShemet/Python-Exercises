import turtle
rings = {'blue':(-90,0), 'green':(47,-70), 'black':(0,0), 'red':(90,0), 'yellow':(-55,-70)}
turtle.pensize(5)
turtle.speed(7)
for i in rings:
  turtle.penup()
  turtle.goto(rings[i])
  turtle.pendown()
  turtle.color(i)
  turtle.circle(50)
turtle.exitonclick()