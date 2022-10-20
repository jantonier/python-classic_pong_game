from turtle import Turtle

# Coordinates:
INITIAL_X_RIGHT = 350
INITIAL_X_LEFT = -350
INITIAL_Y = 0

# Degrees:
UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(1, 5)
        if position.lower() == 'left' or position.lower() == "left":
            self.goto(INITIAL_X_LEFT, INITIAL_Y)
        else:
            self.goto(INITIAL_X_RIGHT, INITIAL_Y)
        self.setheading(UP)

    def move_up(self):
        self.setheading(UP)
        self.forward(20)

    def move_down(self):
        self.setheading(DOWN)
        self.forward(20)


