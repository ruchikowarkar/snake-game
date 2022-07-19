from turtle import Turtle, Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)

food.drop_food()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.snake[0].distance(food) < 15:
        food.drop_food()
        snake.increase_length(snake.last_x(), snake.last_y())
        scoreboard.increase_score()

    if snake.snake[0].xcor() >= 300 or snake.snake[0].xcor() <= -300 or snake.snake[0].ycor() >= 300 or snake.snake[0].ycor() <= -300:
        scoreboard.reset()
        snake.reset()

    for i in range(1, len(snake.snake)):
        if snake.snake[0].distance(snake.snake[i]) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
