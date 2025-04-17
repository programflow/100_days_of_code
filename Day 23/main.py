from turtle import Screen
import time
from player import Player
import carmanager
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


player = Player()
car_manager = carmanager.CarManager()
car_manager.generate_car()
scoreboard = Scoreboard()
screen.onkeypress(player.walk, "w")

game_is_on = True
while game_is_on:
    car_manager.generate_car()

    car_manager.move_cars()
    car_manager.remove_car()
    # Detect player collision with car
    for car in car_manager.cars:
        if player.distance(car)< 20:
            game_is_on = False
    # detect if player reached the other side
    if player.ycor() > 320:
        scoreboard.increase_level()
        player.reset_position()
        car_manager.chance += 5
        car_manager.car_speed += 1

    time.sleep(0.05)
    screen.update()


scoreboard.game_over()




screen.exitonclick()