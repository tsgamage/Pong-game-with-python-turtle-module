import time
from turtle import Screen
from paddles import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

right_paddle = Paddle(-390,0)

_game_running = True
while _game_running:
    time.sleep(0.1)
    right_paddle.move(-240,240)



screen.exitonclick()