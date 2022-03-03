from turtle import Turtle
import random

COLORS = [
    "HotPink", "DeepPink", "SeaGreen", "MediumAquamarine", "DarkSeaGreen", "SteelBlue", "CadetBlue",
    "CornflowerBlue", "RoyalBlue", "SkyBlue", "Tomato", "LightCoral", "Gold", "Khaki",
    "DarkKhaki", "Crimson", "Violet", "MediumPurple"
]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self, starting_x, y_axis):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.all_tires = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.y_top = y_axis[1] - 20
        self.y_bottom = y_axis[0] + 20
        self.x_right = starting_x

    def generate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(self.y_bottom, self.y_top)
            new_car.setheading(180)
            if len(self.all_cars) < 10:
                random_x = random.randint(100, 200)
                new_car.goto(random_x, random_y)
            elif len(self.all_cars) < 20:
                random_x = random.randint(200, 300)
                new_car.goto(random_x, random_y)
            else:
                new_car.goto(self.x_right, random_y)

            upper_tire = Turtle("square")
            upper_tire.hideturtle()
            upper_tire.penup()
            upper_tire.shapesize(stretch_wid=0.2, stretch_len=0.5)
            upper_tire.pensize(3)
            upper_tire.pencolor("#680f18")
            upper_tire.setheading(new_car.heading())

            lower_tire = Turtle("square")
            lower_tire.hideturtle()
            lower_tire.penup()
            lower_tire.shapesize(stretch_wid=0.2, stretch_len=0.5)
            lower_tire.pensize(3)
            lower_tire.pencolor("#680f18")
            lower_tire.setheading(new_car.heading())

            upper_tire.goto(new_car.xcor(), new_car.ycor() + 10)
            lower_tire.goto(new_car.xcor(), new_car.ycor() - 10)

            self.all_tires.append(upper_tire)
            self.all_tires.append(lower_tire)
            self.all_cars.append(new_car)

    def generate_starting_traffic(self):
        num_of_cars = 30
        for num in range(num_of_cars):
            self.generate_car()

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)
        for tire in self.all_tires:
            tire.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

