from turtle import Turtle

UP =90
DOWN =270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.head = Turtle()
        self.head.shape("square")
        self.head.color("white")
        self.head.penup()
        self.head.speed(1)

        self.x_cor = self.head.xcor()
        self.y_cor = self.head.ycor()
        self.snake_body = []
        self.create_body()

    def create_body(self):
        for i in range(0,2):
            self.grow_snake((self.x_cor-20*(i+1), self.y_cor))



    def grow_snake(self,position):
        new_tail = Turtle("square")
        new_tail.color("white")
        new_tail.penup()
        new_tail.speed(1)
        new_tail.goto(position)
        self.snake_body.append(new_tail)

    def extend(self):
        tail_position = self.snake_body[-1].xcor(), self.snake_body[-1].ycor()
        self.grow_snake(tail_position)

    def move(self):
        prev_x = self.x_cor
        prev_y = self.y_cor
        self.head.forward(20)
        self.x_cor = self.head.xcor()
        self.y_cor = self.head.ycor()


        for i in range(len(self.snake_body)):

            if i == 0:
                temp_x = self.snake_body[i].xcor()
                temp_y = self.snake_body[i].ycor()
                self.snake_body[i].goto(prev_x, prev_y)
                prev_x = temp_x
                prev_y = temp_y
            else:
                temp_x = self.snake_body[i].xcor()
                temp_y = self.snake_body[i].ycor()
                self.snake_body[i].goto(prev_x, prev_y)
                prev_x = temp_x
                prev_y = temp_y

    def go_left(self):
        if self.head.heading() != RIGHT :
            self.head.setheading(LEFT)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def reset_snake(self):
        for seg in self.snake_body:
            seg.goto(1000, 1000)
        self.snake_body.clear()
        self.head.goto(0,0)
        self.create_body()