from turtle import Turtle

SCOREBOARD_FONT = ("courier", 48, "normal")


class Scoreboard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.teleport(x, y)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(self.score, move=False, align="center", font=SCOREBOARD_FONT)

    def add_a_point(self):
        self.score += 1
        self.update_score()