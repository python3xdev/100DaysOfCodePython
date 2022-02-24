import turtle
from turtle import Turtle
from random import choice


class SpecialEnemy(Turtle):  # 11x5 grid
    def __init__(self, game, positions, enemy_image):
        super().__init__()
        self.game = game
        self.starting_positions = tuple(positions)
        self.position = list(choice(self.starting_positions))
        self.enemy_image = enemy_image
        self.enemy_points = [50, 100, 150, 200, 300]
        self.killed = True
        self.MOVE_SPEED = 0.4
        self.directions = {'left': -1, 'right': 1}
        self.direction = 'left' if tuple(self.position) == self.starting_positions[0] else 'right'
        self.create_enemy()

    def create_enemy(self):
        self.penup()
        self.goto(self.position)
        self.color('red')
        turtle.register_shape(self.enemy_image)
        self.shape(self.enemy_image)
        self.setheading(90)
        self.hide_from_player()

    def render(self):
        self.move()
        self.goto(self.position)

    def die(self):
        self.hide_from_player()
        self.hideturtle()
        self.game.player_ui.player_score += choice(self.enemy_points)

    def hide_from_player(self):
        self.killed = True
        self.goto(-self.game.SW // 2 - 100, -self.game.SH // 2 - 100)
        self.position = list(choice(self.starting_positions))
        self.direction = 'left' if tuple(self.position) == self.starting_positions[0] else 'right'
        self.hideturtle()

    def move(self):
        self.position[0] += self.MOVE_SPEED * self.directions[self.direction]
        if self.position[0] > self.game.SW//2 + 150:
            self.hide_from_player()
            pass
        if self.position[0] < -self.game.SW//2 - 150:
            self.hide_from_player()
            pass
