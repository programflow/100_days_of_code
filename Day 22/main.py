from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

from scoreboard import Scoreboard




screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()
paddle_1 = Paddle((-350, 0))
paddle_2 = Paddle((350, 0))
ball = Ball()

# Paddle 1 controls
screen.onkey(paddle_1.move_up, "w")
screen.onkey(paddle_1.move_down, "s")
# Paddle 2 controls
screen.onkey(paddle_2.move_up, "Up")
screen.onkey(paddle_2.move_down, "Down")



def restart_game():
    scoreboard.score_1 = 0
    scoreboard.score_2 = 0
    scoreboard.update_score()
    ball.reset_pos()


screen.onkey(restart_game, "r")





#Start the game
game_on = True
while game_on:
    screen.update()

    ball.move()
    # Detect Wall Collision
    if ball.ycor() <= -280 or ball.ycor() >= 280:
        ball.bounce_y()
    # Detect paddle collision
    if (ball.distance(paddle_1) < 50 and ball.xcor()<-340) or (ball.distance(paddle_2) < 50 and ball.xcor() > 340):
        ball.bounce_x()

    # Add points if ball hits vertical walls
    if ball.xcor() < -400:
        scoreboard.score_2 += 1
        scoreboard.update_score()
        ball.reset_pos()

    elif ball.xcor() > 400:
        scoreboard.score_1 += 1
        scoreboard.update_score()
        ball.reset_pos()

    if scoreboard.score_1 == 5 or scoreboard.score_2 == 5:
        game_is_on = False
        scoreboard.game_over()

    time.sleep(ball.move_speed)
screen.exitonclick()

#TODO: Create the Screen
#TODO: Create and move a paddle
#TODO: Create another paddle
#TODO: Create the ball and make it move
#TODO: Detect collision with wall and bounce
#TODO: Detect collision with paddle
#TODO: Detect when paddle misses
#TODO: Keep Score