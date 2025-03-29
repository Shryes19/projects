from turtle import Turtle, Screen
from middle_design import Middle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
middle = Middle()

screen.bgcolor('black')
screen.screensize(800, 600)
screen.tracer(0)

for k in range(22):
    middle.block()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

is_on = True
while is_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset()
        ball.bounce_x()
        scoreboard.l_point()


    if ball.xcor() <  -380:
        ball.reset()
        ball.bounce_x()
        scoreboard.r_point()

screen.exitonclick()
