# from tkinter import *
from turtle import *

tim = Turtle()
screen = Screen()
screen.tracer(0)
tim.penup()
y = -250
tim.goto(-350,y)
tim.pendown()

is_on = True
c = 0
k = 1

while k<11:
    c += 1
    for _ in range(4):
        tim.forward(40)
        tim.right(90)
    if c < 10:
        tim.forward(40)
    else:
        tim.penup()
        c = 0
        y = y + 40
        k += 1
        tim.goto(-350,y)
        tim.pendown()

    screen.update()

screen.exitonclick()

# window = Tk()
# window.title("Snake&Ladder")
#
# window.mainloop()
