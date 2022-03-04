from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, paddle_color, position, move_speed):
        super().__init__()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.shape("square")
        self.color(paddle_color)
        self.penup()
        self.goto(position)
        self.move_speed = move_speed

    def go_up(self):
        new_y = self.ycor() + self.move_speed
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - self.move_speed
        self.goto(self.xcor(), new_y)
