from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from pygame import mixer
import time

# Music!
mixer.init()
mixer.music.load("music/background-music.mp3")
mixer.music.play()

# Set up the screen
screen = Screen()
screen.bgcolor("black")
screen.title("Classic Ping Pong")
screen.setup(800, 600)
screen.tracer(0)

# Initialize components
paddle_r = Paddle('right')
paddle_l = Paddle('left')
ball = Ball()
score = Scoreboard()

# Initialize keyboard controllers
screen.listen()
screen.onkey(paddle_r.move_up, "Up")
screen.onkey(paddle_r.move_down, "Down")
screen.onkey(paddle_l.move_up, "a")
screen.onkey(paddle_l.move_down, "z")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.05)
    game_is_on = ball.check_for_wall_collision()

    # Detect when a paddle misses, update the score and reset the ball
    if not game_is_on:
        if ball.xcor() > 0:
            score.left_score_up()
        else:
            score.right_score_up()
        ball.reset()
        sleep_time = .01
        screen.update()
        time.sleep(1)
        game_is_on = True

    # Detect collision with paddles
    if (ball.distance(paddle_r) < 50 and ball.xcor() > 320) or (ball.distance(paddle_l) < 50 and ball.xcor() < -320):
        ball.bounce_x()

screen.exitonclick()
