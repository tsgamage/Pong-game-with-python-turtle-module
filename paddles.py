from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y, paddle_color = "white"):
        super().__init__()
        self.y = y
        self.x = x
        self.shape("square")
        self.shapesize(5,1)
        self.color(paddle_color)
        self.penup()
        self.teleport(x,y)
        self.speed("slowest")

    def move(self,y_from, y_to):
        self.goto(self.x,y_from)
        self.goto(self.x,y_to)
