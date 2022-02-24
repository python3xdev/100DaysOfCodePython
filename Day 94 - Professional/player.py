import turtle
from turtle import Turtle


class Player(Turtle):
    def __init__(self, game, position):
        super().__init__()
        self.game = game
        self.starting_position = tuple(position)
        self.position = position
        self.cooldown_protection = False
        self.create_player()

    def remove_cooldown(self):
        print("Invincibility has been removed!")
        self.cooldown_protection = False

    def create_player(self):
        self.penup()
        self.goto(self.position)
        self.color('white')
        turtle.register_shape("art/spaceship.gif")
        self.shape("art/spaceship.gif")
        self.setheading(90)

    def render(self):
        self.goto(self.position)

    def move(self, event):
        self.position[0] = event.x - (self.game.SW // 2)

    def shoot(self, x, y):
        if self.game.bullet.can_shoot:
            self.game.bullet.position = [self.position[0], self.position[1]]
            self.game.bullet.showturtle()
            self.game.bullet.can_shoot = False

    def die(self):
        self.game.player_ui.player_lives -= 1

    # def restart(self):
    #     self.goto(self.starting_position)
