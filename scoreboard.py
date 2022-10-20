import turtle
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 240)
        self.score_left = 0
        self.score_right = 0
        self.update_score()

    def left_score_up(self):
        self.score_left += 1
        self.update_score()

    def right_score_up(self):
        self.score_right += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(str(self.score_left) + "  " + str(self.score_right), align="center", font=("Courier", 60, "normal"))
