from turtle import Turtle, Screen, colormode
from random import randint, choice

# colors = ["CornflowerBlue","DarkGrey","DarkSeaGreen","DeepPink","DarkGreen","IndianRed4", "DarkOrchid4"]
angles = [0, 90, 180, 270]

timmy = Turtle()
timmy.shape()
timmy.speed(6)
timmy.pensize(10)
colormode(255)

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r,g,b)

for i in range(100):
    # timmy.color(choice(colors))
    timmy.color(random_color())

    timmy.forward(30)
    timmy.left(choice(angles))
