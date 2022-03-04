from turtle import Turtle


class MiddleLine(Turtle):
    def __init__(self, color, pen_size, height):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color(color)
        self.pensize(pen_size)
        self.draw_line_from = height / -2 + 2
        self.draw_line_to = height / 2 + 10
        self.setposition(x=0, y=self.draw_line_from)
        self.setheading(90)

    def draw(self):
        while self.ycor() < self.draw_line_to:
            new_y = self.ycor() + 20
            self.pendown()
            self.goto(self.xcor(), new_y)
            self.penup()
            self.goto(self.xcor(), new_y + 18)
