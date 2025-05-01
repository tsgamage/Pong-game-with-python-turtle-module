import time
from turtle import Screen
from paddles import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle(360, 0)
left_paddle = Paddle(-370, 0)

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

    ball.move()

    # Delect if the ball hits the top and bottom
    if ball.ycor() > 285 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect if the ball hits the paddle
    collapse_with_right_paddle = 335 < ball.xcor() < 355 and ball.distance(right_paddle) < 50
    collapse_with_left_paddle = -355 > ball.xcor() > -375 and ball.distance(left_paddle) < 50

    if collapse_with_right_paddle or collapse_with_left_paddle:
        ball.bounce_x()


    # Detect if the ball missed by a paddle
    ball_pass_right_paddle = ball.xcor() > 400
    ball_pass_left_paddle = ball.xcor() < -400

    if ball_pass_right_paddle:
        ball.missed("right")

    if ball_pass_left_paddle:
        ball.missed("left")

screen.exitonclick()