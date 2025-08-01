import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        y_pos = random.randint(-270, 250)
        new_car.goto(x=270, y=y_pos)
        self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            new_x = car.xcor() - self.car_speed
            car.goto(new_x, car.ycor())

    def level_up(self):
        for car in self.all_cars:
            car.hideturtle()
            car.clear()
            car.goto(1000, 1000)
        self.all_cars = []
        self.car_speed += MOVE_INCREMENT



