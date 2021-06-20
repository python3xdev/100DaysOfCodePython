"""
import turtle
from turtle import Turtle
from turtle import *
import turtle as t
"""

from turtle import Turtle, Screen

tim = Turtle()

tim.color("SeaGreen4")
for i in range(4):
    tim.forward(100)
    tim.right(90)

screen = Screen()
screen.exitonclick()
