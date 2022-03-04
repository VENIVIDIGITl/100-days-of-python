from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from table import MiddleLine
import time

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 400
TOP_WALL = int(SCREEN_HEIGHT / 2) - 20
BOTTOM_WALL = int(SCREEN_HEIGHT / -2) + 20
RIGHT_END = int(SCREEN_WIDTH / 2)
LEFT_END = int(SCREEN_WIDTH / -2)
TABLE_COLOR = "black"
SCOREBOARD_COLOR = "LightSteelBlue"
MIDDLE_LINE_COLOR = "LightSteelBlue"
BALL_COLOR = "lavender"
PADDLE_COLOR = "lavender"
PADDLE_MOVE_SPEED = 30

screen = Screen()
screen.title("PONG")
screen.bgcolor(TABLE_COLOR)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)
middle_line = MiddleLine(color=MIDDLE_LINE_COLOR, pen_size=3, height=SCREEN_HEIGHT)
middle_line.draw()

r_paddle = Paddle(paddle_color=PADDLE_COLOR, position=(RIGHT_END - 50, 0), move_speed=PADDLE_MOVE_SPEED)
l_paddle = Paddle(paddle_color=PADDLE_COLOR, position=(LEFT_END + 50, 0), move_speed=PADDLE_MOVE_SPEED)
ball = Ball(BALL_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT)
scoreboard = Scoreboard(color=SCOREBOARD_COLOR, scoreboard_y_position=TOP_WALL - 80)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall.
    if ball.ycor() > TOP_WALL or ball.ycor() < BOTTOM_WALL:
        ball.bounce_y()

    # Detect collision with paddle.
    if ball.distance(r_paddle) < 50 and ball.xcor() > RIGHT_END-80 \
            or ball.distance(l_paddle) < 50 and ball.xcor() < LEFT_END+80:
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() > RIGHT_END:
        ball.reset_position()
        scoreboard.score(side="left")

    # Detect when left paddle misses
    if ball.xcor() < LEFT_END:
        ball.reset_position()
        scoreboard.score(side="right")
