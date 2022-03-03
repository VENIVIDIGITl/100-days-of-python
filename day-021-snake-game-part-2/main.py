from turtle import Screen
import time
from border import draw_border
from snake import Snake
from food import Food
from scoreboard import Scoreboard
WIDTH = 470
HEIGHT = 310
SCOREBOARD_XCOR = int(WIDTH / -2 + 23)
SCOREBOARD_YCOR = int(HEIGHT / 2 - 33)

screen = Screen()
screen.title("SNEK")
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("#617c69")
screen.tracer(0)

draw_border("#2b2d2b", 5, WIDTH, HEIGHT)
snake = Snake()
food = Food()
food.area_width = WIDTH
food.area_height = HEIGHT
scoreboard = Scoreboard()
scoreboard.goto(SCOREBOARD_XCOR, SCOREBOARD_YCOR)
scoreboard.update_scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        print("NOM NOM NOM")
        food.refresh(segments=snake.segments)
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() < WIDTH / -2 + 16 or snake.head.xcor() > WIDTH / 2 - 22 \
            or snake.head.ycor() < HEIGHT / -2 + 20 or snake.head.ycor() > HEIGHT / 2 - 40:
        scoreboard.reset()
        snake.reset()
        food.refresh(segments=snake.segments)

    # Detect collision with tail.
    for segment in snake.segments[2:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
