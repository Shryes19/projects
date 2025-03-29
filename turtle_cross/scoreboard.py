FONT = ("Courier", 10, "normal")
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(-230,250)
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def inc_score(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score}",align="center",font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=("Courier", 26,"normal"))
