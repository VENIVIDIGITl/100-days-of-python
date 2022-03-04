from turtle import Turtle


class Ball(Turtle):
    def __init__(self, color, width, height):
        super().__init__()
        self.turtlesize(stretch_wid=1, stretch_len=1)
        self.shape("circle")
        self.color(color)
        self.penup()
        self.screen_width = width
        self.screen_height = height
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def increase_move_speed(self):
        self.move_speed *= 0.8

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.increase_move_speed()

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
