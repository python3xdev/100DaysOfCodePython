import turtle as t
import random

tim = t.Turtle()
tim.left(90)
tim.speed('fastest')

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    result = (r, g, b)
    return result

def draw():
    deg = 360
    space = 5
    loop = int(deg/space)
    for i in range(loop):
        tim.pencolor(random_color())
        tim.circle(75)
        tim.left(5)


draw()

screen = t.Screen()
screen.exitonclick()
