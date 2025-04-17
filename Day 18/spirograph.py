import turtle as t
import random





tim = t.Turtle()
tim.speed(0)
t.colormode(255)
t.pensize(100)

number_of_circles = 15
angle = 360/number_of_circles

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)


for _ in range(number_of_circles):
    tim.color(random_color())
    tim.circle(radius=100)
    tim.left(angle)