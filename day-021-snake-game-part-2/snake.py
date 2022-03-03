from turtle import Turtle
STARTING_POSITIONS = [(-3, 0), (-17, 0), (-37, 0), (-57, 0), (-77, 0)]
MOVE_DISTANCE = 20
PEN_SIZE = 15
SEGMENT_LENGTH = 0.7
SEGMENT_WIDTH = 0.7
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("#2b2d2b")
        new_segment.shapesize(stretch_len=SEGMENT_LENGTH, stretch_wid=SEGMENT_WIDTH)
        new_segment.pensize(PEN_SIZE)
        new_segment.pencolor("#2b2d2b")
        new_segment.penup()
        new_segment.goto(position)
        new_segment.seg_position = position
        new_segment.dist = new_segment.distance
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.clear()
            seg.penup()
            seg.goto(9999, 9999)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        # Add a new segment to the snake.
        self.add_segment(self.segments[-1].position())

    def move(self):
        self.segments[::-1].clear()
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].clear()
            self.head.clear()
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].setheading(self.segments[seg_num - 1].heading())
            self.segments[seg_num].pendown()
            if seg_num == len(self.segments) - 1:
                self.segments[seg_num].penup()
                self.segments[seg_num].clear()
            self.segments[seg_num].goto(new_x, new_y)

        for seg in self.segments:
            seg.penup()
            seg.pendown()

        self.head.forward(MOVE_DISTANCE)
        self.head.shapesize(stretch_len=SEGMENT_LENGTH, stretch_wid=SEGMENT_WIDTH)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head .setheading(RIGHT)
