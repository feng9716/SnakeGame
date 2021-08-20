from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("Snake Game")

snake = Snake()
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

screen.exitonclick()
