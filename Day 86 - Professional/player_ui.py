from turtle import Turtle


class PlayerUI:
    def __init__(self):
        self.player_score = 0
        self.player_lives = 3
        self.player_ui_turtle = Turtle()
        self.create_ui()

    def create_ui(self):
        self.player_ui_turtle.penup()
        self.player_ui_turtle.hideturtle()
        self.player_ui_turtle.color("white")

        self.player_ui_turtle.goto(-390, 230)
        self.player_ui_turtle.write(f"Score: {self.player_score}", align="left", font=("Calibri", 45, "normal"))

        self.player_ui_turtle.goto(190, 230)
        self.player_ui_turtle.write(f"Lives: {self.player_lives}", align="left", font=("Calibri", 45, "normal"))

    def render(self):
        self.player_ui_turtle.clear()
        self.player_ui_turtle.goto(-390, 230)
        self.player_ui_turtle.write(f"Score: {self.player_score}", align="left", font=("Calibri", 45, "normal"))

        self.player_ui_turtle.goto(190, 230)
        self.player_ui_turtle.write(f"Lives: {self.player_lives}", align="left", font=("Calibri", 45, "normal"))

    def game_over(self):
        self.player_ui_turtle.goto(0, -15)
        self.player_ui_turtle.write(f"GAME OVER", align="center", font=("Calibri", 45, "normal"))

        self.player_ui_turtle.goto(0, -30)
        self.player_ui_turtle.write(f"Click Anywhere To Exit", align="center", font=("Calibri", 15, "normal"))

    def win(self):
        self.player_ui_turtle.goto(0, -15)
        self.player_ui_turtle.write(f"YOU WIN", align="center", font=("Calibri", 45, "normal"))

        self.player_ui_turtle.goto(0, -30)
        self.player_ui_turtle.write(f"Click Anywhere To Exit", align="center", font=("Calibri", 15, "normal"))
