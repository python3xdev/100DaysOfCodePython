from turtle import Turtle, Screen

distance = 10
turn_degree = 5
tim = Turtle()


def move_forwards():
    tim.forward(distance)


def move_backwards():
    tim.backward(distance)


def turn_left():
    tim.left(turn_degree)


def turn_right():
    tim.right(turn_degree)


def clear():
    tim.reset()


screen = Screen()
screen.listen()

screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear)

screen.exitonclick()
