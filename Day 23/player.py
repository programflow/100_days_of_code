from turtle import Turtle

STARTING_POSITION = (0, -280)

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.reset_position()
        self.setheading(90)

    def walk(self):
        self.forward(10)

    def reset_position(self):
        self.goto(STARTING_POSITION)

