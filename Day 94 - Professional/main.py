import turtle
from turtle import Screen
from random import randint

from player import Player
from bullet import Bullet
from enemy import Enemy
from player_ui import PlayerUI
from special_enemy import SpecialEnemy


class Game:
    def __init__(self):
        self.screen = Screen()
        self.screen.title("Space Invaders")
        self.screen.bgcolor("#000000")
        self.SW, self.SH = 800, 600
        self.screen.setup(self.SW, self.SH)
        self.screen.cv._rootwindow.resizable(False, False)
        self.screen.tracer(0)

        self.enemy_type_by_row = {'1': "art/alien1.gif", '2': "art/alien1.gif", '3': "art/alien2.gif",
                                  '4': "art/alien2.gif", '5': "art/alien3.gif"}

        # creating instances
        self.player = Player(self, [0, -240])
        self.bullet = Bullet(self, [0, -240])
        self.player_ui = PlayerUI(self)

        self.enemies = []
        self.enemy_wave = 1
        self.enemy_start_y = 270
        self.create_enemies()

        self.special_enemy = SpecialEnemy(self, ((self.SW//2 + 100, 210), (-self.SW//2 - 100, 210)), "art/alien4.gif")

        # binding the mouse motion and clicks
        self.canvas = turtle.getcanvas()
        self.canvas.bind("<Motion>", self.player.move)
        self.screen.onscreenclick(self.player.shoot)

    def create_enemies(self):
        column_pad, row_pad = 0, 0
        for row in range(1, 6):
            for column in range(1, 12):
                next_type = self.enemy_type_by_row[str(row)]
                if next_type == "art/alien1.gif":
                    self.enemies.append(Enemy(self, [column * 50 - 413 + column_pad, row * 15 + self.SH//2 - self.enemy_start_y + row_pad], next_type, 10))
                elif next_type == "art/alien2.gif":
                    self.enemies.append(Enemy(self, [column * 50 - 413 + column_pad, row * 15 + self.SH//2 - self.enemy_start_y + row_pad], next_type, 20))
                elif next_type == "art/alien3.gif":
                    self.enemies.append(Enemy(self, [column * 50 - 413 + column_pad, row * 15 + self.SH//2 - self.enemy_start_y + row_pad], next_type, 40))
                column_pad += 5
            column_pad = 0
            row_pad += 20

        self.player.cooldown_protection = True
        self.screen.ontimer(self.player.remove_cooldown, 5000)

    def next_wave(self):
        self.enemies.clear()
        self.create_enemies()
        # self.player_ui.player_lives += 1  # this would make the game way to easy

    def run(self):
        while self.player_ui.player_lives:
            self.screen.update()
            self.player.render()
            self.player_ui.render()
            if (randint(0, 2500) == 1) and self.special_enemy.killed:
                self.special_enemy.killed = False
                self.special_enemy.showturtle()

            if not self.special_enemy.killed:
                if self.bullet.check_collision(self.special_enemy):
                    self.bullet.hide_bullet()
                    self.special_enemy.die()
                self.special_enemy.render()

            any_enemy_alive = None
            for enemy in self.enemies:
                if not enemy.killed:
                    any_enemy_alive = True
                    enemy.render()
                    if not enemy.active_bullet.can_shoot:  # rendering the bullet if it has been shot
                        enemy.active_bullet.render()

                    if enemy.active_bullet.check_collision(self.player):  # checking if bullet collides with player
                        enemy.active_bullet.hide_bullet()
                        for e in self.enemies:
                            e.active_bullet.hide_bullet()
                        if not self.player.cooldown_protection:
                            self.player.die()
                            self.player.cooldown_protection = True
                            self.screen.ontimer(self.player.remove_cooldown, 3000)  # 3 seconds of invincibility

                    if self.bullet.check_collision(enemy):  # checking players bullet collision with enemy
                        self.bullet.hide_bullet()
                        enemy.die()

            if not any_enemy_alive:
                self.next_wave()

            if not self.bullet.can_shoot:
                self.bullet.render()

        self.player_ui.game_over()
        self.screen.exitonclick()


if __name__ == "__main__":
    game = Game()
    game.run()
