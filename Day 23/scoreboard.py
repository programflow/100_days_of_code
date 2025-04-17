from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.level = 0
        self.increase_level()

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="left", font=("Arial", 24, "normal"))

    def game_over(self):
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 30, "normal"))

