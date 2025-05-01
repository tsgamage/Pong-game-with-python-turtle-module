import time
from turtle import Turtle, Screen

screen = Screen()

class Paddle(Turtle):
    def __init__(self, x, y, paddle_color = "white"):
        super().__init__()
        self.y = y
        self.x = x
        self.shape("square")
        self.shapesize(1,5)
        self.setheading(90)
        self.color(paddle_color)
        self.penup()
        self.teleport(x,y)
        self.speed("slowest")

    def move(self,y_from, y_to):

        self.goto(self.x, y_from)
        self.goto(self.x, y_to)


    def go_up(self, distance=10):
        if self.ycor() < 250:
            current_y = self.ycor()
            new_y = current_y + distance
            self.goto(self.x,new_y)

    def go_down(self, distance=10):
        if self.ycor() > -240:
            current_y = self.ycor()
            new_y = current_y - distance
            self.goto(self.x, new_y)