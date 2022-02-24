import turtle
from player import Player
from brick import Brick
from ball import Ball
from player_ui import PlayerUI
# from sound_manager import SoundManager  # game freezes while sound is playing. Thats why I commented out all the sound_manager parts... I tried many libraries.

screen = turtle.Screen()
screen.title("Brick Breaker!")
screen.bgcolor("#000000")
SW, SH = 800, 600
screen.setup(SW, SH)
screen.tracer(0)

# creating instances
player = Player([25, -250])
bricks = []
brick_colors_by_row = {'1': "yellow", '2': "yellow", '3': "green", '4': "green", '5': "orange", '6': "orange", '7': "red", '8': "red"}
column_pad, row_pad = 0, 0
for row in range(1, 9):
    for column in range(1, 15):
        next_color = brick_colors_by_row[str(row)]
        if next_color == "yellow":
            bricks.append(Brick((column * 50 - 413 + column_pad, row * 15 + SH//2 - 250 + row_pad), next_color, 1))
        elif next_color == "green":
            bricks.append(Brick((column * 50 - 413 + column_pad, row * 15 + SH//2 - 250 + row_pad), next_color, 3))
        elif next_color == "orange":
            bricks.append(Brick((column * 50 - 413 + column_pad, row * 15 + SH//2 - 250 + row_pad), next_color, 5))
        elif next_color == "red":
            bricks.append(Brick((column * 50 - 413 + column_pad, row * 15 + SH//2 - 250 + row_pad), next_color, 7))
        column_pad += 5
    column_pad = 0
    row_pad += 5

ball = Ball()
player_ui = PlayerUI()
# sound_manager = SoundManager()

canvas = turtle.getcanvas()
canvas.bind('<Motion>', player.move)

running = True
out = True

while bricks and player_ui.player_lives:  # either no more bricks, or no more lives
    screen.update()
    player.render()
    player_ui.render()

    if (ball.xcor() >= SW//2 or ball.xcor() <= -SW//2) and out:
        out = False
        ball.bounce_x()
        # sound_manager.wall_hit()
    if ball.ycor() >= SH//2:
        out = True
        ball.bounce_y()
        # sound_manager.wall_hit()
    if ball.ycor() <= -SH//2:
        out = True
        ball.reset_ball()
        player_ui.player_lives -= 1

    if ball.distance(player) <= 60 and ball.ycor() <= -250:
        out = True
        ball.bounce_y()
        # sound_manager.player_hit()

    for brick in bricks:
        if ball.distance(brick) <= 20 and ball.ycor() <= brick.ycor():
            out = True
            ball.bounce_y(True)
            brick.reset()
            bricks.remove(brick)
            player_ui.player_score += brick.points
            # sound_manager.brick_hit()
        if ball.distance(brick) <= 20 and ball.xcor() <= brick.xcor():
            out = True
            ball.bounce_x()
            brick.reset()
            bricks.remove(brick)
            player_ui.player_score += brick.points
            # sound_manager.brick_hit()

    ball.move()

if player_ui.player_lives == 0:
    player_ui.game_over()
elif not bricks:
    player_ui.win()

screen.exitonclick()
