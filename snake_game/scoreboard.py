from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as high:
            self.h = int(high.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.h}", align="center", font=("Arial", 24, "normal"))

    def high_score(self):
        if self.score > self.h:
            self.h = self.score
            with open("data.txt", "w") as high:
                high.write(f"{self.h}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))

    def inc_score(self):
        self.score += 1
        self.update_score()
