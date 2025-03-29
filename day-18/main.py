import random
import turtle
from turtle import Turtle,Screen

timmy_the_turtle = Turtle()
turtle.colormode(255)
timmy_the_turtle.shape("turtle")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

timmy_the_turtle.pensize(5)
timmy_the_turtle.speed("fastest")

for i in range(int(360/5)):
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.circle(100)
    timmy_the_turtle.setheading(timmy_the_turtle.heading() + 5)

screen = Screen()
screen.exitonclick()