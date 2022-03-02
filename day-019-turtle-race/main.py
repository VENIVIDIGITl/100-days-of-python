from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.title("TURTLE RACE")
screen.setup(width=500, height=400)
screen.bgcolor("#2c3e50")
user_bet = screen.textinput(title="Make your bet",
        prompt="Which turtle will win the race, blue, purple, red, orange, cyan or black? Enter a color: ")

colors = ["blue", "purple", "red", "orange", "cyan", "black"]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    # new_turtle.speed("fastest")
    new_turtle.color(colors[turtle_index], "green")
    new_turtle.penup()
    y = -65 + (turtle_index * 30)
    new_turtle.goto(x=-230, y=y)
    all_turtles.append(new_turtle)

result = Turtle()
result.color("#a7c7e7")
result.hideturtle()
result.penup()
result.goto(0, 100)
result.clear()

finish_line = Turtle()
finish_line.hideturtle()
finish_line.pencolor("white")
finish_line.penup()
finish_line.goto(200, -145)
finish_line.left(90)
finish_line.pensize(7)
finish_line.pendown()
finish_line.forward(300)
finish_line.penup()
finish_line.right(90)
finish_line.forward(14)
finish_line.write("🏁", align="center", font=("Courier", 30, "normal"))
finish_line.goto(215, -155)
finish_line.write("🏁", align="center", font=("Courier", 30, "normal"))

bet = Turtle()
bet.hideturtle()
bet.pencolor("lavender")
bet.penup()
bet.goto(0, -180)
bet.write(f"Your bet: {user_bet}", align="center", font=("Courier", 22, "normal"))


if user_bet:
    is_race_on = True

while is_race_on:
    top3 = []
    for turtle in all_turtles:
        if turtle.xcor() > 200:
            is_race_on = False
            winning_color = turtle.pencolor()
            top3.append(turtle.pencolor())

        random_distance = random.randint(1, 30)
        turtle.forward(random_distance)

    if len(top3) > 2:
        result.goto(0, 0)
        result.write(f"🥇 {top3[0]}\n🥈 {top3[1]}\n🥉 {top3[2]}", align="center", font=("Courier", 22, "normal"))
    elif len(top3) > 1:
        result.goto(0, 0)
        result.write(f"🥇 {top3[0]}\n🥈 {top3[1]}", align="center", font=("Courier", 22, "normal"))
    elif len(top3) > 0:
        result.goto(0, 0)
        result.write(f"🥇 {top3[0]}", align="center", font=("Courier", 22, "normal"))

    if len(top3) > 0 and top3[0] == user_bet:
        result.goto(0, 80)
        result.write("YOU WIN!", align="center", font=("Courier", 28, "bold",))
    elif len(top3) > 0 and top3[0] != user_bet:
        result.goto(0, 80)
        result.write("YOU LOSE!", align="center", font=("Courier", 28, "bold",))

screen.exitonclick()
