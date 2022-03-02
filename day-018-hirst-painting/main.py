import turtle as turtle_module
import random

turtle_module.colormode(255)
screen = turtle_module.Screen()
t = turtle_module.Turtle()
t.speed("fastest")
t.penup()
t.hideturtle()

color_list = [(58, 106, 148), (224, 200, 109), (134, 84, 58), (223, 138, 62), (196, 145, 171), (234, 226, 204),
              (224, 234, 230), (141, 178, 204), (139, 82, 105), (209, 90, 69), (188, 80, 120), (68, 105, 90),
              (237, 225, 233), (134, 182, 136), (133, 133, 74), (63, 156, 92), (48, 156, 194), (183, 192, 201),
              (214, 177, 191), (19, 57, 93), (21, 68, 113), (112, 123, 149), (229, 174, 165), (172, 203, 182),
              (158, 205, 215), (69, 58, 47), (108, 47, 60), (53, 70, 65), (72, 64, 53), (134, 42, 38), (47, 66, 61),
              (0, 122, 125)]

t.setheading(223)
t.forward(317)
t.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    t.dot(20, random.choice(color_list))
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

screen.exitonclick()
