from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, cords):
        super().__init__()
        self.WIDTH = 20
        self.HEIGHT = 100
        self.cords = cords
        self.create_paddle()

    def create_paddle(self):
        self.penup()
        self.setheading(90)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(self.cords)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
