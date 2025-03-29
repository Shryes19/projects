import random
import turtle
from turtle import Turtle,Screen
turtle.colormode(255)
tim = Turtle()

color_list = [(211, 159, 115), (137, 158, 186), (152, 85, 44), (43, 109, 156), (21, 47, 69), (218, 201, 125), (74, 107, 78), (113, 88, 97), (144, 165, 153), (187, 136, 164), (79, 35, 24), (171, 152, 57), (125, 30, 19), (167, 9, 15), (59, 166, 74), (6, 48, 45), (29, 65, 106), (216, 182, 174), (78, 81, 36), (166, 193, 220), (57, 31, 34), (151, 111, 119), (180, 109, 88), (112, 126, 151), (172, 206, 183), (217, 176, 191)]
tim.penup()
tim.speed("fastest")
tim.hideturtle()
tim.backward(250)
tim.right(90)
tim.forward(200)
tim.left(90)
for i in range(1,101):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if i % 10 == 0:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(500)
        tim.setheading(0)
screen = Screen()
screen.exitonclick()
