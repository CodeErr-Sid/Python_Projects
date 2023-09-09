import time
import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard  import Scoreboard
import time


screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong!")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddles
    c1 = ball.distance(r_paddle) < 50 and ball.xcor() > 320
    c2 = ball.distance(l_paddle) < 50 and ball.xcor() > -330
    if c1:
        ball.bounce_x()

    if c2:
        ball.bounce_x()


    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
