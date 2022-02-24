from turtle import Turtle


class Bullet(Turtle):
    def __init__(self, game, position):
        super().__init__()
        self.position = position
        self.can_shoot = True
        self.game = game
        self.MOVE_SPEED = 3
        self.create_bullet()

    def create_bullet(self):
        self.penup()
        self.goto(self.position)
        self.color('white')
        self.shape("square")
        self.shapesize(0.15, 0.5)
        self.setheading(90)
        self.hide_bullet()

    def render(self):
        self.move()
        self.goto(self.position)
        if self.position[1] > (self.game.SH // 2):
            self.hide_bullet()

    def hide_bullet(self):
        self.can_shoot = True
        self.goto(self.game.SW // 2 - 10, -self.game.SH // 2 + 10)
        self.hideturtle()

    def move(self):
        self.position[1] += self.MOVE_SPEED

    def check_collision(self, col_obj):
        return abs(self.xcor() - col_obj.xcor()) < 20 and abs(self.ycor() - col_obj.ycor()) < 20
