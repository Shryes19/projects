from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.st_position = [(0, 0), (-20, 0), (-40, 0)]
        self.l = []
        self.create_snake()
        self.head = self.l[0]
        self.head.shape("square")

    def create_snake(self):
        for position in self.st_position:
            self.add_seg(position)

    def add_seg(self, position):
        tim = Turtle("square")
        tim.penup()
        tim.color("green")
        tim.goto(position)
        self.l.append(tim)


    def reset(self):
        for seg in self.l:
            seg.goto(1000,1000)
        self.l.clear()
        self.create_snake()
        self.head = self.l[0]

    def extend(self):
        self.add_seg(self.l[-1].position())

    def move(self):
        for r in range(len(self.l) - 1, 0, -1):
            x_cor = self.l[r - 1].xcor()
            y_cor = self.l[r - 1].ycor()
            self.l[r].goto(x_cor, y_cor)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
