import turtle as t
import random
import colorgram

def set_up():
    t.shape("circle")
    t.speed(9)
    t.penup()
    t.hideturtle()
    t.goto(-250,250)


def random_color():
    specific_color =random.choice(colors)
    r = specific_color.rgb[0]
    g = specific_color.rgb[1]
    b = specific_color.rgb[2]
    return (r,g,b)

colors = colorgram.extract('kirby.jpg', 30)
t.screensize(500,500)
set_up()
t.colormode(255)



for j in range(9):
    t.goto(-250, 250 - 50*(j+1))
    for i in range(9):
        t.color(random_color())
        t.forward(50)
        t.stamp()



t.exitonclick()