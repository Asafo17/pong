from turtle import Turtle
from random import randint


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x = self.xcor()
        self.y = self.ycor()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.x + self.x_move
        new_y = self.y + self.y_move
        self.goto(new_x, new_y)
        self.x = new_x
        self.y = new_y

    def bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1

    def reset_ball(self):
        self.x = 0
        self.y = 0
        self.goto(self.x, self.y)
        self.paddle_bounce()

    def increase_speed(self):
        self.x_move += 2
        self.y_move += 2