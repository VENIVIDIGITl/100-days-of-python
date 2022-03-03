from turtle import Turtle
SCOREBOARD_ALIGNMENT = "left"
GAME_OVER_ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("#2b2d2b")
        self.penup()
        self.shapesize(3)
        self.goto(0, 999)
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"HIGH SCORE: {self.high_score}\t SCORE: {self.score}", align=SCOREBOARD_ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 7
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()
