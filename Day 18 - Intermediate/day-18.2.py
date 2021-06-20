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
          'lawngreen',
          'LightSeaGreen',
          'turquoise',
          'violet',
          'RoyalBlue'
]

t = Turtle()

def calc_deg(sides):
    return 360/sides

def draw(sides):
    color = choice(colors)
    deg = calc_deg(sides)
    for side in range(sides):
        t.pencolor(color)
        t.forward(100)
        t.right(deg)

for i in range(3, 11):
    draw(i)

screen = Screen()
screen.exitonclick()
