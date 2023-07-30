from turtle import Screen
from paddle import Paddles
from scoreboard import ScoreBoard
from ball import Ball
from time import sleep
import random

screen = Screen()
screen.setup(height=600, width=1000)
screen.bgcolor('black')
screen.tracer(0)

num = [-1, 1]

paddles = Paddles()
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(paddles.left_up, 'w')
screen.onkey(paddles.left_down, 's')
screen.onkey(paddles.right_up, 'Up')
screen.onkey(paddles.right_down, 'Down')

game_on = True
collision = False
x = 1
y = 1

while game_on:
    screen.update()
    sleep(0.03)
    ball.move()

    if ball.y >= 290 or ball.y <= -290:
        ball.bounce()

    if ball.distance(paddles.right_paddle) < 50 and ball.x >= 430 or ball.distance(paddles.left_paddle) < 50 \
            and ball.x <= -430:
        ball.paddle_bounce()
        ball.increase_speed()

    if ball.x > 480:
        scoreboard.score_left += 1
        scoreboard.score_l()
        ball.reset_ball()

    if ball.x < -480:
        scoreboard.score_right += 1
        scoreboard.score_r()
        ball.reset_ball()


screen.exitonclick()