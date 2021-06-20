from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

"""
!!!
WE ARE USING .onkeypress, THIS ALLOWS THE PLAYER TO HOLD DOWN THE KEYS TO CONTINUOUSLY MOVE THE PADDLE.
IF YOU USE .onkey, THIS WILL REQUIRE THE PLAYER TO PUSH THE KEYS MULTIPLE TIMES...
!!!
"""
# first paddle
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
# second paddle
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect ball collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detect ball collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect ball colliding with the walls behind the paddles...
    if ball.xcor() > 360:
        ball.reset_ball()
        scoreboard.increase_l_score()
        game_speed = 0.1

    elif ball.xcor() < -360:
        ball.reset_ball()
        scoreboard.increase_r_score()
        game_speed = 0.1


screen.exitonclick()
