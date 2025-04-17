from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
timmy_the_turtle.speed(3)

colors = ["CornflowerBlue","DarkGrey","DarkSeaGreen","DeepPink","DarkGreen","IndianRed4", "DarkOrchid4"]

def draw_polygon(sides):
    sum_of_angle = (sides-2)*180
    each_angle = 180 - sum_of_angle/sides
    for i in range(sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(each_angle)


for n in range(0, 7):
    timmy_the_turtle.pencolor(colors[n])
    draw_polygon(n+3)

screen = Screen()
screen.exitonclick()