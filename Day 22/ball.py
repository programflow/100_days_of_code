from turtle import Turtle
import random
MOVE_DISTANCE = 5

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.step_x = MOVE_DISTANCE
        self.step_y = MOVE_DISTANCE
        self.move_speed =0.1

    def move(self):
        new_x = self.xcor() + self.step_x
        new_y = self.ycor() + self.step_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        variation = random.uniform(0.9, 1.1) *-1
        self.step_y *= variation


    def bounce_x(self):
        variation = random.uniform(0.9, 1.1) *-1
        self.step_x *= -1
        self.move_speed *= 0.9

    def reset_pos(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1

