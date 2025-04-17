from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.score_1 = 0
        self.score_2 = 0
        self.update_score()

    def update_score(self):
        self.clear()
        print(self.score_1)
        self.write(f"{self.score_1}        {self.score_2}", align="center", font=("Arial", 20, "bold"))





