import turtle
from turtle import Turtle
from random import randint


class Enemy(Turtle):  # 11x5 grid
    def __init__(self, game, position, enemy_image, enemy_points):
        super().__init__()
        self.game = game
        self.starting_position = tuple(position)
        self.position = position
        self.enemy_image = enemy_image
        self.enemy_points = enemy_points
        self.killed = False
        self.active_bullet = EnemyBullet(self.game, [self.position[0], self.position[1]])
        self.MOVE_SPEED = 0.2
        self.create_enemy()

    def create_enemy(self):
        self.penup()
        self.goto(self.position)
        self.color('white')
        turtle.register_shape(self.enemy_image)
        self.shape(self.enemy_image)
        self.setheading(90)

    def render(self):
        self.move()
        self.goto(self.position)

    def die(self):
        self.killed = True
        self.active_bullet.hide_bullet()
        self.goto(-self.game.SW // 2 - 100, -self.game.SH // 2 - 100)
        self.hideturtle()
        self.game.player_ui.player_score += self.enemy_points

    def move(self):
        self.position[0] += self.MOVE_SPEED
        if self.position[0] > self.starting_position[0] + 165:
            self.MOVE_SPEED *= -1
            self.position[1] -= 35
        if self.position[0] < self.starting_position[0]:
            self.MOVE_SPEED *= -1
            self.position[1] -= 35

        if self.position[1] < -self.game.SH//2 + 80:
            self.game.player_ui.player_lives = 0

        if randint(0, 3000) == 1:
            self.shoot()

    def shoot(self):
        self.active_bullet.can_shoot = True
        if self.active_bullet.can_shoot:
            self.active_bullet.position = [self.position[0], self.position[1]]
            self.active_bullet.showturtle()
            self.active_bullet.can_shoot = False


class EnemyBullet(Turtle):
    def __init__(self, game, position):
        super().__init__()
        self.position = position
        self.can_shoot = False
        self.game = game
        self.MOVE_SPEED = 1.5
        self.create_bullet()

    def create_bullet(self):
        self.penup()
        self.goto(self.position)
        self.color('white')
        turtle.register_shape("art/rocket.gif")
        self.shape("art/rocket.gif")
        self.setheading(-90)
        self.hide_bullet()

    def render(self):
        self.move()
        self.goto(self.position)
        if self.position[1] < -self.game.SH:
            self.hide_bullet()

    def hide_bullet(self):
        self.can_shoot = False
        self.goto(-self.game.SW // 2, self.game.SH // 2)
        self.hideturtle()

    def move(self):
        self.position[1] -= self.MOVE_SPEED

    def check_collision(self, col_obj):
        # return abs(self.xcor() - col_obj.xcor()) < 15 and abs(self.ycor() - col_obj.ycor()) < 15
        return self.distance(col_obj) < 15
