from turtle import Turtle

UP = 90


class Brick(Turtle):
    def __init__(self, position, color, points):
        super().__init__()
        self.position = position
        self.brick_color = color
        self.points = points
        self.create_brick()

    def create_brick(self):
        self.penup()
        self.goto(self.position)
        self.color(self.brick_color)
        self.shape('square')
        self.setheading(UP)
        self.shapesize(2, 0.5)