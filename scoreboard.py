from turtle import Turtle


class ScoreBoard:

    def __init__(self):
        self.line = Turtle(shape='square')
        self.left = Turtle(shape='square')
        self.right = Turtle(shape='square')
        self.line.hideturtle()
        self.left.hideturtle()
        self.right.hideturtle()
        self.left.color('white')
        self.right.color('white')
        self.middle_line()
        self.score_left = 0
        self.score_right = 0
        self.score_r()
        self.score_l()

    def middle_line(self):
        y = 310
        self.line.pensize(5)
        for i in range(30):
            y -= 10
            self.line.goto(0, y)
            self.line.color('black')
            y -= 10
            self.line.goto(0, y)
            self.line.color('white')
        self.line.penup()

    def score_l(self):
        self.left.clear()
        self.left.penup()
        self.left.goto(-100, 240)
        self.left.pendown()
        self.left.write(self.score_left, align='center', font=('Courier', 30, 'bold'))

    def score_r(self):
        self.right.clear()
        self.right.penup()
        self.right.goto(100, 240)
        self.right.pendown()
        self.right.write(self.score_right, align='center', font=('Courier', 30, 'bold'))