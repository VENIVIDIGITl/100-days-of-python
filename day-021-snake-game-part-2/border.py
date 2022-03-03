from turtle import Turtle

border = Turtle()


def draw_border(color, border_width, width, height):
    x_min = width / -2 + 16
    x_max = width / 2 - 22
    y_min = height / -2 + 20
    y_max = height / 2 - 40

    border.hideturtle()
    border.color(color)
    border.pensize(border_width)
    border.speed("fastest")
    border.penup()
    border.goto(x_min, y_max)
    border.pendown()
    border.goto(x_max, y_max)
    border.goto(x_max, y_min)
    border.goto(x_min, y_min)
    border.goto(x_min, y_max)
    border.penup()
