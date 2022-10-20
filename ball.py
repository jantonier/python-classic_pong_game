from turtle import Turtle

STEP = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_direction = 'right'
        self.y_direction = 'up'
        self.setpos(0, 0)

    def move(self):
        if self.x_direction == 'right' and self.y_direction == 'up':
            self.setheading(45)
            self.forward(10)
        elif self.x_direction == 'right' and self.y_direction == 'down':
            self.setheading(315)
            self.forward(10)
        elif self.x_direction == 'left' and self.y_direction == 'down':
            self.setheading(225)
            self.forward(10)
        else:
            self.setheading(135)
            self.forward(10)

    def bounce_y(self):
        if self.y_direction == 'down':
            self.y_direction = 'up'
        else:
            self.y_direction = 'down'

    def bounce_x(self):
        if self.x_direction == 'right':
            self.x_direction = 'left'
        else:
            self.x_direction = 'right'
        self.speed(10)

    def check_for_wall_collision(self):
        if self.xcor() > 380:
            self.bounce_x()
            self.bounce_y()
            return False
        if self.ycor() > 280:
            self.bounce_y()
        if self.xcor() < -380:
            self.bounce_x()
            self.bounce_y()
            return False
        if self.ycor() < -280:
            self.bounce_y()
        return True

    def reset(self):
        self.goto(0, 0)
