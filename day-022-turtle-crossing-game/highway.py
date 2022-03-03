from turtle import Turtle


class Highway(Turtle):
    def __init__(self, width, height):
        super().__init__()
        self.shape("square")
        self.hideturtle()
        self.pensize(3)
        self.penup()
        self.color("grey")
        self.setheading(0)
        self.line_length = width + 50
        self.highway_width = height - 50
        self.num_of_lanes = 7
        self.lane_width = self.highway_width / self.num_of_lanes

    def draw(self):
        self.draw_edges()
        self.draw_lines()

    def draw_lines(self):
        x_start = self.line_length / 2 - 10
        x_end = self.line_length / -2 + 10
        y_bottom = self.highway_width / -2 + 50
        y_start = y_bottom + self.lane_width / 2
        self.color("LightGrey")
        self.penup()
        self.goto(x_start, y_start)
        self.setheading(180)

        while self.ycor() < self.highway_width / 2 - 50:
            while self.xcor() > x_end:
                self.pendown()
                self.forward(40)
                self.penup()
                self.forward(60)
            self.goto(x_start, self.ycor() + self.lane_width)

    def draw_edges(self):
        x_start = self.line_length / 2
        x_end = self.line_length / -2
        y_bottom = self.highway_width / -2 + 50
        y_top = self.highway_width / 2 - 50
        self.color("grey")
        self.goto(x_start, y_bottom)
        self.pendown()
        self.goto(x_end, y_bottom)
        self.penup()
        self.goto(x_start, y_top)
        self.pendown()
        self.goto(x_end, y_top)
        self.penup()
