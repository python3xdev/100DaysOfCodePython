from turtle import Turtle
from datetime import datetime


class PlayerUI(Turtle):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.my_font = "Press Start 2P"  # to be able to see the font, please install it! It is located in the fonts dir
        self.player_score = 0
        self.player_lives = 3
        self.create_ui()

    def create_ui(self):
        self.hideturtle()
        self.penup()
        self.color('white')

        self.render()

    def render(self):
        self.clear()
        self.goto(-self.game.SW // 2 + 10, self.game.SH // 2 - 60)
        self.write(f"SCORE:{self.player_score}", font=(self.my_font, 25, "normal"), align='left')

        self.goto(self.game.SW // 2 - 250, self.game.SH // 2 - 60)
        self.write(f"LIVES:{self.player_lives}", font=(self.my_font, 25, "normal"), align='left')

    def game_over(self):
        with open('score_history.txt', 'a') as f:
            data = f'{datetime.now().strftime("%B %d, %Y | %I:%M:%S %p")} -> SCORE: {self.player_score}\n'
            print(data)
            f.write(data)
            print("Your score has been saved!".title())
