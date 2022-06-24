from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong Game")

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)

scoreboard = Scoreboard()

ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    #Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()
    #Detect right paddle miss
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.left_scored()
    #Detect left paddle miss
    elif ball.xcor() < -400:
        ball.reset_position()
        scoreboard.right_scored()
screen.exitonclick()
