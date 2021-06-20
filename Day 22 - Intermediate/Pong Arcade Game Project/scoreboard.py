from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.draw_line()
        self.penup()
        self.draw()

    def draw_line(self):
        self.goto(0, 290)
        self.setheading(270)
        self.width(3)
        for i in range(14):
            self.forward(20)
            self.pendown()
            self.forward(20)
            self.penup()

    def draw(self):
        self.clear()
        self.draw_line()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 70, "bold"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 70, "bold"))

    def increase_l_score(self):
        self.l_score += 1
        self.draw()

    def increase_r_score(self):
        self.r_score += 1
        self.draw()
