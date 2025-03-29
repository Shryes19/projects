from turtle import Turtle,Screen
import random

# timmy = Turtle(shape="turtle")
# timmy.speed("fastest")
s=-100
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race. Enter a color")
colors = ["red", "orange", "yellow", "blue", "green", "purple"]
l = []
is_on = True

for r in range(6):
   timmy = Turtle(shape="turtle")
   timmy.color(colors[r])
   timmy.penup()
   timmy.goto(-230, s)
   l.append(timmy)
   s += 50

while is_on:
    for turtle in l:
     r = random.randint(0,10)
     turtle.forward(r)
     if turtle.xcor() > 230:
         is_on = False
         winning_color = turtle.pencolor()
         if user_bet == winning_color:
             print(f"You've won! The {winning_color} turtle is the winner!")
         else:
             print(f"You've lost! The {winning_color} turtle is the winner!")




screen.exitonclick()