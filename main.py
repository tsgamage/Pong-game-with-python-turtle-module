import time
from turtle import Screen
from paddles import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle(360,0)
left_paddle = Paddle(-370,0)

ball = Ball()

screen.listen()

screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")

_game_running = True
while _game_running:
    time.sleep(0.005)
    screen.update()







screen.exitonclick()