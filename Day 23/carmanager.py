from turtle import Turtle
import random
CAR_COLORS =["red", "orange", "yellow", "green", "cyan", "blue", "purple"]

class Car(Turtle):
    def __init__(self, position, c_speed):
        super().__init__()
        self.car_speed = c_speed
        self.shape("square")
        self.penup()
        self.color(random.choice(CAR_COLORS))
        self.goto(position)
        self.turtlesize(stretch_wid=1, stretch_len=2)

    def move(self):
        self.forward(self.car_speed)




class CarManager:
    def __init__(self):
        self.cars = []
        self.chance = 20
        self.car_speed = 2

    def generate_car(self):

        if random.randint(1,1000) <= self.chance:
            position = (-340,random.randint(-12, 12)*20)
            self.cars.append(Car(position, self.car_speed))
            print("generated Car")

    def move_cars(self):
            for car in self.cars:
                car.move()


    def remove_car(self):
        if len(self.cars) > 0:
            for i in self.cars:
                if i.xcor() >= 340 :
                    self.cars.remove(i)
                    print("removed car")
