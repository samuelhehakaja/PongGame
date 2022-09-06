from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from boundaries import Boundaries
from scoreboard import Scoreboard

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
screen = Screen()
ball = Ball()
boundaries = Boundaries()
scoreboard = Scoreboard()
screen.tracer(0)
game_on = True
score1 = 0
score2 = 0

screen.screensize(canvwidth=800, canvheight=600)
screen.bgcolor("black")
screen.title("Pong")

screen.listen()
screen.onkey(fun=right_paddle.move_up, key="Up")
screen.onkey(fun=right_paddle.move_down, key="Down")
screen.onkey(fun=left_paddle.move_up, key="w")
screen.onkey(fun=left_paddle.move_down, key="s")

while game_on:
    ball.move()
    screen.update()
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.wall_bounce()
    if ball.xcor() > 390:
        ball.reset_round()
        score1 += 1
        scoreboard.add_score(score1, score2)
    elif ball.xcor() < -390:
        ball.reset_round()
        score2 += 1
        scoreboard.add_score(score1, score2)
    elif ball.xcor() >= 330 and ball.distance(right_paddle.pos()) <= 50 or ball.xcor() <= -330 and ball.distance(
            left_paddle.pos()) <= 50:
        ball.paddle_bounce()

screen.exitonclick()
