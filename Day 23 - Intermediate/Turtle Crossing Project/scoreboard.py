from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.FONT = ("Courier", 24, "bold")
        self.penup()
        self.color("black")
        self.hideturtle()
        self.draw_level()

    def draw_level(self):
        self.goto(-290, 260)
        self.write(f"Level: {self.level}", align="left", font=self.FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.draw_level()

    def game_over(self):
        self.home() # go to the center
        self.write("GAME OVER", align="center", font=self.FONT)
