from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, color, scoreboard_y_position):
        super().__init__()
        self.color(color)
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.scoreboard_y_position = scoreboard_y_position
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, self.scoreboard_y_position)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, self.scoreboard_y_position)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def score(self, side):
        if side == "left":
            self.l_score += 1
        elif side == "right":
            self.r_score += 1
        self.update_score()
