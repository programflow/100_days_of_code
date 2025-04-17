from turtle import Turtle, Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard

# sets up the display screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)



# set up different aspects of game
snek = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(fun = snek.go_left,key= "Left")
screen.onkey(fun = snek.go_right,key= "Right")
screen.onkey(fun = snek.go_up,key= "Up")
screen.onkey(fun = snek.go_down,key= "Down")
screen.listen()





game_on = True
speed = .2
while game_on:

    screen.update()
    time.sleep(speed)
    snek.move()


    if snek.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snek.extend()
        speed -= .02

    if snek.head.xcor() >280 or snek.head.xcor() <-280 or snek.head.ycor() > 280 or snek.head.ycor() <-280:
        game_on = False
        print("Wall collision")

    for snek_seg in snek.snake_body:
        if snek_seg.distance(snek.head) < 15:
            game_on = False
            print("Snek collision")
            break

scoreboard.game_over()
screen.exitonclick()