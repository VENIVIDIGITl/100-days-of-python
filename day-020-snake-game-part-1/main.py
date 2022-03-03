from turtle import Screen, Turtle
import time
from border import draw_border
from snake import Snake

screen = Screen()
screen.title("SNEK")
screen.setup(width=900, height=600)
screen.bgcolor("#617c69")
screen.tracer(0)

draw_border(Turtle(), "#2b2d2b", 5, screen.window_width(), screen.window_height())
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.07)
    snake.move()

screen.exitonclick()
