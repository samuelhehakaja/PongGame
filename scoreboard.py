from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", "30", "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.add_score(0, 0)

    def add_score(self, score1, score2):
        self.clear()
        self.write(f"{score1}       {score2}", align=ALIGNMENT, font=FONT)