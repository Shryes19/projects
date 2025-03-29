from turtle import Turtle


class Middle:

    def __init__(self):
        self.c = 300

    def block(self):

        for i in range(2):
            tim = Turtle("square")
            tim.color("white")
            tim.shapesize(0.3)
            tim.penup()
            tim.goto(0, self.c)
            self.c = self.c - 7

        for r in range(2):
            tim = Turtle("square")
            tim.color("black")
            tim.shapesize(0.3)
            tim.penup()
            tim.goto(0, self.c)
            self.c = self.c - 7
#def right_block(self):
