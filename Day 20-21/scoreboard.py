from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 10, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.retrieve_highscore()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def record_highscore(self, new_highscore):
        with open("data.txt", "w") as file:
            file.write(f"{new_highscore}")

    def retrieve_highscore(self):
        with open("data.txt", "r") as file:
            new_highscore = file.read()
            return int(new_highscore)

    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.record_highscore(self.highscore)
        self.score = 0
        self.update_scoreboard()