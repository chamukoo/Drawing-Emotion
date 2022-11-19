# Programmed by: Lee Anne Y. Angeles

import turtle
s = turtle.Screen()
t = turtle.Turtle(shape='turtle')
t.color('orange','yellow')

t.begin_fill()
t.circle(100)
t.end_fill()
t.penup()

t.color('black', 'red')
# left eye
t.goto(-30, 135)
t.pendown()
t.dot(20)
t.penup()

# right eye
t.goto(30, 135)
t.pendown()
t.dot(20)
t.penup()

# mouth
t.goto(-60, 60)
t.pendown()
t.setheading(-60)
t.circle(70, 120)