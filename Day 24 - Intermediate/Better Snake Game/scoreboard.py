from turtle import Turtle

SCOREBOARD_X_POS = 0
SCOREBOARD_Y_POS = 260

ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(SCOREBOARD_X_POS, SCOREBOARD_Y_POS)
        self.score = 0
        with open('data.txt') as file:
            data = int(file.read())
            self.high_score = data
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", 'w') as file:
                file.write(str(self.score))
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
