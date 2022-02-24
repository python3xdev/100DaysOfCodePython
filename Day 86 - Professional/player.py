from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90


class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.lives = 3
        self.position = position
        self.create_paddle()

    def create_paddle(self):
        self.penup()
        self.goto(self.position)
        self.color("white")
        self.shape('square')
        self.setheading(UP)
        self.shapesize(3, 0.5)

    def render(self):
        self.goto(self.position)

    def move(self, event):
        self.position[0] = event.x - 405