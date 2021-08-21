from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)

score = Scoreboard()

screen.bgcolor("black")
screen.title("Snake Game")

snake = Snake()
screen.update()

food = Food()
screen.update()

screen.listen()
screen.onkey(snake.head_up, "Up")
screen.onkey(snake.head_down, "Down")
screen.onkey(snake.head_left, "Left")
screen.onkey(snake.head_right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.07)
    snake.move()

    if snake.head.distance(food) < 15:
        # generate new food
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
