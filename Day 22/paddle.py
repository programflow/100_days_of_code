from turtle import Turtle



class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.color("white")
        self.shape("square")

        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(coordinates)

    def move_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)


    def move_down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)


