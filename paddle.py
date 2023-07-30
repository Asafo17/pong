from turtle import Turtle


class Paddles:

    def __init__(self):
        self.left_paddle = Turtle(shape='square')
        self.left_paddle.shapesize(stretch_wid=3, stretch_len=1)
        self.left_paddle.color('white')
        self.left_paddle.penup()
        self.left_paddle.goto(-450, 0)

        self.right_paddle = Turtle(shape='square')
        self.right_paddle.shapesize(stretch_wid=3, stretch_len=1)
        self.right_paddle.color('white')
        self.right_paddle.penup()
        self.right_paddle.goto(450, 0)

    def right_up(self):
        self.right_paddle.goto(450, self.right_paddle.ycor() + 30)

    def right_down(self):
        self.right_paddle.goto(450, self.right_paddle.ycor() - 30)

    def left_up(self):
        self.left_paddle.goto(-450, self.left_paddle.ycor() + 30)

    def left_down(self):
        self.left_paddle.goto(-450, self.left_paddle.ycor() - 30)
