from turtle import Turtle, Screen
from random import choice

colors = ['cyan',
          'brown',
          'DarkGreen',
          'lime',
          'DeepPink',
          'DarkGrey',
          'gold',
          'DeepSkyBlue2',
          'Firebrick1',
          'LightSeaGreen',
          'turquoise',
          'violet',
          'RoyalBlue'
]

directions = [0, 90, 180, 270]

t = Turtle()
distance = 30
t.pensize(13)
t.speed('fastest')


def run():
    while True:
        color = choice(colors)
        direction = choice(directions)
        t.pencolor(color)
        t.setheading(direction)
        t.forward(distance)


run()

screen = Screen()
screen.exitonclick()
