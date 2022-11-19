# Programmed by: Lee Anne Y. Angeles

import turtle

print("========== EMOTIONS ==========")
print("\t1 --> Happy")
print("\t2 --> Sad")
print("\t3 --> Angry")
print("\t4 --> Surprised")
print("")
emotion = int(input("How are you feeling today? "))

s = turtle.Screen()
t = turtle.Turtle(shape='turtle')
t.color('black','yellow')
t.pensize(5)

if emotion == 3:
    t.color('black', 'red')
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    t.penup()

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

    #mouth
    t.goto(60, 60)
    t.pendown()
    t.setheading(120)
    t.circle(70, 120)

if emotion in (1,2,4):
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    t.penup()

    t.color('black', 'blue')
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
    if emotion == 1:
        t.goto(-60, 60)
        t.pendown()
        t.setheading(-60)
        t.circle(70, 120)

    elif emotion == 2:
        t.goto(60, 60)
        t.pendown()
        t.setheading(120)
        t.circle(70, 120)

    elif emotion == 4:
        t.penup()
        t.goto(0, 30)
        t.pendown()

        t.begin_fill()
        t.fillcolor('black')
        t.circle(30)
        t.end_fill()
        t.penup()