import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("Snake Game!")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # detect collision with wall
    x = snake.head.xcor()
    y = snake.head.ycor()
    if x > 280 or x < -280 or y > 280 or y < -280:
        game_on = False
        score.game_over()

    # detect collision with tail
    for segment in snake.segments[1::]:
      if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()


screen.exitonclick()
