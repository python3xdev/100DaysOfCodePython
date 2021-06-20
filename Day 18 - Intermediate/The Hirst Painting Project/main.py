# import colorgram
#
# colors_extracted = colorgram.extract('image.jpg', 17)
# colors = []
#
# for i in colors_extracted:
#     r = i.rgb[0]
#     g = i.rgb[1]
#     b = i.rgb[2]
#     color = (r, g, b)
#     colors.append(color)
#
# print(colors)

import turtle as t
from random import choice

RADIUS = 20
SPACE = 50

tim = t.Turtle()
tim.speed('fastest')
tim.hideturtle()
t.colormode(255)

color_list = [(203, 34, 66),
              (71, 116, 151),
              (228, 161, 193),
              (150, 184, 70),
              (151, 160, 164),
              (242, 235, 46),
              (37, 161, 80),
              (35, 31, 32),
              (137, 205, 187),
              (240, 99, 54),
              (75, 65, 40),
              (33, 162, 165),
              (221, 49, 65)
              ]


def new_color():
    return choice(color_list)


def new_line():
    tim.up()
    tim.backward(500)
    tim.left(90)
    tim.forward(50)
    tim.right(90)
    tim.down()


def first_position():
    tim.up()
    tim.right(90)
    tim.forward(250)
    tim.right(90)
    tim.forward(235)
    tim.right(180)
    tim.down()


def draw_dots():
    first_position()
    for i in range(10):
        if i != 0:
            new_line()
        for j in range(10):
            color = new_color()
            tim.fillcolor(color)
            tim.begin_fill()
            tim.circle(RADIUS)
            tim.end_fill()
            tim.up()
            tim.forward(SPACE)
            tim.down()


draw_dots()
screen = t.Screen()
screen.exitonclick()
