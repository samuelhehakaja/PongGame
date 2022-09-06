from turtle import Turtle


class Boundaries(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.goto(-400, -300)
        self.pendown()
        for i in range(2):
            self.forward(800)
            self.left(90)
            self.forward(600)
            self.left(90)