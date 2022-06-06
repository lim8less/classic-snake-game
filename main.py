import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

scoreboard = Scoreboard()
food = Food()
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.moves()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        print("nom nom")
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall
    # if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
    #     game_is_on = False
    #     score.game_over()

    # NO WALLS
    if snake.head.xcor() > 295:
        ycor = snake.head.ycor()
        snake.head.goto(-295.0, ycor)
    elif snake.head.xcor() < -295:
        ycor = snake.head.ycor()
        snake.head.goto(295.0, ycor)
    if snake.head.ycor() > 295:
        xcor = snake.head.xcor()
        snake.head.goto(xcor, -295.0)
    elif snake.head.ycor() < -295:
        xcor = snake.head.xcor()
        snake.head.goto(xcor, 295.0)

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

    # Respawn food if it spawns on snake segments
    for segment in snake.segments[1:]:
        if segment.distance(food) < 15:
            food.refresh()


screen.exitonclick()
