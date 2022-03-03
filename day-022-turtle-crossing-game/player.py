from turtle import Turtle
import random

MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self, starting_y, finish_line_y):
        super().__init__()
        self.shape("turtle")
        self.color("Lime", "Green")
        self.penup()
        self.setheading(90)
        self.start_position = (0, starting_y + 5)
        self.finish_line_y = finish_line_y
        self.go_to_start()

    def move_up(self):
        if self.heading() == 90:
            self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > self.finish_line_y:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(self.start_position)

    def squish(self, effect):
        if effect == "collision":
            self.spin()
            self.color("crimson", "green")
            self.pencolor("#680f18")
            self.turtlesize(1)

        elif effect == "death":
            self.color("crimson", "red")
            self.pencolor("#680f18")

    def spin(self):
        for num in range(1, 4):
            self.pendown()
            self.pencolor("#680f18")
            self.pensize(random.randint(4, 16))
            random_x = self.xcor() - random.randint(8, 16)
            random_y = self.ycor() + random.randint(-8, 8)
            self.setheading(self.heading() - 77)
            self.goto(random_x, random_y)
