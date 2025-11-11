from turtle import Turtle , Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.tracer(0)

left_paddle = Paddle(-350 , 0)
right_paddle = Paddle(350 , 0)
ball = Ball()
left_scoreboard = Scoreboard(-200 , 280)
right_scoreboard = Scoreboard(200 , 280)


screen.listen()

screen.onkey(right_paddle.go_up , "Up")
screen.onkey(right_paddle.go_down , "Down")
screen.onkey(left_paddle.go_up , "w")
screen.onkey(left_paddle.go_down , "s")


screen_is_on = True
while screen_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #detect ball collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.y_bounce()
    #ball collision with paddle
    if ball.distance(right_paddle)<50 and ball.xcor()>340 or ball.distance(left_paddle)<50 and ball.xcor()<-340:
        ball.x_bounce()
    if ball.xcor()>380:
        right_scoreboard.increase_score()
        ball.reset_position()
    if ball.xcor() < -380:
        left_scoreboard.increase_score()
        ball.reset_position()


    



screen.exitonclick()
