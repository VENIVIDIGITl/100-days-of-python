import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from highway import Highway
import time

WIDTH, HEIGHT = 800, 600
BOTTOM = HEIGHT / -2
TOP = HEIGHT / 2
X_AXIS = (WIDTH / 2 - 20, WIDTH / -2 + 20)
Y_AXIS = (BOTTOM+50, TOP-50)
SCOREBOARD_XCOR = int(WIDTH / -2 + 25)
SCOREBOARD_YCOR = int(HEIGHT / 2 - 35)

screen = Screen()
screen.title("TURTLE CROSSING")
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)
screen.bgcolor("black")

highway = Highway(width=WIDTH, height=HEIGHT)
highway.draw()
car_manager = CarManager(starting_x=WIDTH / 2, y_axis=Y_AXIS)
car_manager.generate_starting_traffic()
player = Player(starting_y=BOTTOM + 20, finish_line_y=TOP-20)
scoreboard = Scoreboard()
scoreboard.goto(SCOREBOARD_XCOR, SCOREBOARD_YCOR)
scoreboard.update_scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

ending_countdown = 50
game_is_on = True
player_is_dead = False

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.generate_car()
    car_manager.move_cars()

    if ending_countdown == 0:
        print("You died")

        scoreboard.game_over()
        game_is_on = False

    elif player_is_dead and ending_countdown <= 50:
        ending_countdown -= 1
        if ending_countdown < 35:
            player.squish(effect="death")
            for tire in car_manager.all_tires:
                if tire.distance(player) < 20:
                    tire.pencolor("#b41b2a")
                    tire.pendown()

    for tire in car_manager.all_tires:
        random_length = random.randint(60, 130)
        if tire.distance(player) > random_length:
            tire.penup()

    # Detect when the turtle collides with a car.
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            for tire in car_manager.all_tires:
                if player.distance(tire) < 13:
                    tire.pendown()
                    
            if ending_countdown > 35:
                player.squish(effect="collision")
            player_is_dead = True

    # Detect successful crossing.
    if player.is_at_finish_line():
        print(f"FINISHED LEVEL: {scoreboard.level}")
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
