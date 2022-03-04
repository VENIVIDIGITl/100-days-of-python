from turtle import Turtle

FONT = ("Courier", 24, "normal")
GAME_OVER_ALIGNMENT = "center"
SCOREBOARD_ALIGNMENT = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("lavender")

        self.shapesize(3)
        self.goto(0, 999)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align=SCOREBOARD_ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=GAME_OVER_ALIGNMENT, font=FONT)
