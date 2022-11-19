# Programmed by: Lee Anne Y. Angeles

import turtle

while True:
    print("============ EMOTIONS ============")
    print("\n\t1 --> Angry")
    print("\t2 --> Flushed")
    print("\t3 --> Happy")
    print("\t4 --> Sad")
    print("\t5 --> Surprised")
    emotion = int(input("\nHow are you feeling today? "))

    while True:
        print("\n==================================")
        again = input("\nDo you want to try again? (y/n) :").lower()
        if again == 'y':
            break
        elif again == 'n':
            print("\nThank you for using this program!")
            print("\n==================================")
            exit()
        else:
            print("\nInvalid Input! Try again!")
            continue




    s = turtle.Screen()
    t = turtle.Turtle(shape='turtle')
    t.color('black','yellow')
    t.pensize(5)

    if emotion == 1:
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

    elif emotion == 2:
        t.color('black', 'yellow')
        t.begin_fill()
        t.circle(100)
        t.end_fill()
        t.penup()

        # left eye
        t.color('black')
        t.goto(-30, 135)
        t.pendown()
        t.dot(20)
        t.penup()

        # right eye
        t.goto(30, 135)
        t.pendown()
        t.dot(20)
        t.penup()

        # left flush
        t.color('pink')
        t.goto(-40, 100)
        t.pendown()
        t.dot(40)
        t.penup()

        # right flush
        t.goto(40, 100)
        t.pendown()
        t.dot(40)
        t.penup()

        #mouth
        t.color('black')
        t.goto(-60, 60)
        t.pendown()
        t.setheading(-60)
        t.circle(70, 120)


    if emotion in (3,4,5):
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
    