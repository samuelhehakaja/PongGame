from turtle import Turtle

SPEED = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

    def move_up(self):
        y_cor = self.ycor()
        x_cor = self.xcor()
        self.goto(x_cor, y_cor + SPEED)

    def move_down(self):
        y_cor = self.ycor()
        x_cor = self.xcor()
        self.goto(x_cor, y_cor - SPEED)
