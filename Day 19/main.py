import turtle as t
import random

screen = t.Screen()
screen.setup(500, 400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turts = []

def set_up_turtles():
    for i in range(0, len(colors)):
        turts.append(t.Turtle())
        turts[i].shape("turtle")
        turts[i].penup()
        turts[i].color(colors[i])
        # Each turtle
        turts[i].goto(-230, 180 - i*60)

def race_turtles():
    for i in range(0, len(colors)):
        steps_forward = random.randint(1, 10)
        turts[i].forward(steps_forward)

def check_finish_line():
    for i in range(0, len(colors)):
        if turts[i].xcor() >= 230:
            winner = turts[i].color()
            print(f"The winner is {winner[0]}")
            return False, winner[0]
    return True, None

# This sets up the race and asks for a bet
set_up_turtles()
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter a color: ")


racing = True
while racing:
    race_turtles()
    racing, winning_turtle = check_finish_line()
    if not racing:
        if winning_turtle == user_bet.lower():
            print("Your turtle won!")
        else:
            print("Your turtle lost!")











screen.exitonclick()