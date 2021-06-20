from turtle import Turtle, Screen

t = Turtle()

for i in range(15):
    t.forward(10)
    t.up()
    t.forward(10)
    t.down()

screen = Screen()
screen.exitonclick()
