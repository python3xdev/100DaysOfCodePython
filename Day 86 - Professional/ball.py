from turtle import Turtle
from random import choice


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.x_move = self.random_direction()
        self.y_move = 4
        self.create_ball()
        self.reset_ball()

    def random_direction(self):
        return choice([4, -4])

    def create_ball(self):
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(0.5, 0.5)

    def reset_ball(self):
        self.x_move = self.random_direction()
        self.y_move = 4
        self.goto(10, -220)

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self, from_brick=False):
        self.y_move *= -1
        if from_brick:
            self.y_move = (self.y_move * 0.01) + self.y_move
        # print(self.y_move)  # printing ball speed