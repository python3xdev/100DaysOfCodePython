import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.color_list = ['red', 'blue', 'green', 'magenta', 'purple', 'orange', 'yellow']
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        rand_color = random.choice(self.color_list)
        self.color(rand_color)
        self.goto(random_x, random_y)

