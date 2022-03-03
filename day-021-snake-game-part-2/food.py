from turtle import Turtle
import random
FOOD_WIDTH = 0.8
FOOD_HEIGHT = 0.8


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("#2b2d2b")
        self.shapesize(stretch_len=FOOD_HEIGHT, stretch_wid=FOOD_WIDTH)
        self.speed("fastest")
        self.area_width = None
        self.area_height = None
        self.refresh(segments=None, start_coordinates=(random.randint(-70, 70), random.randint(-70, 70)))

    def refresh(self, segments, start_coordinates=None):
        if start_coordinates:
            self.goto(start_coordinates)
        else:
            x_min = int((self.area_width / -2 + 10) * 0.85)
            x_max = int((self.area_width / 2 - 20) * 0.85)
            y_min = int((self.area_height / -2 + 20) * 0.85)
            y_max = int((self.area_height / 2 - 50) * 0.85)

            random_x = random.randint(x_min, x_max)
            random_y = random.randint(y_min, y_max)

            for seg in segments:
                while seg.distance(random_x, random_y) < 50:
                    random_x = random.randint(x_min, x_max)
                    random_y = random.randint(y_min, y_max)

            self.goto(random_x, random_y)
