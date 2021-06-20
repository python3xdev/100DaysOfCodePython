import turtle as t
import random

directions = [0, 90, 180, 270]

tim = t.Turtle()
distance = 30
tim.pensize(13)
tim.speed('fastest')

t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    result = (r, g, b)
    return result


def run():
    while True:
        color = random_color()
        direction = random.choice(directions)
        tim.pencolor(color)
        tim.setheading(direction)
        tim.forward(distance)


run()

screen = t.Screen()
screen.exitonclick()
