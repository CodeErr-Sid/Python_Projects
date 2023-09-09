import random
from turtle import Turtle

COLORS = ["green yellow", "deep pink", "firebrick1", "turquoise1", "magenta2", "SpringGreen2", "DarkGoldenrod"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 6


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_choice = random.randint(1, 5)
        if random_choice == 1:
          new_car =Turtle(shape="square")
          new_car.shapesize(stretch_wid=1, stretch_len=2)
          new_car.penup()
          new_car.color(random.choice(COLORS))
          random_y = random.randint(-250, 250)
          new_car.goto(300, random_y)
          self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def lvl_up(self):
        self.car_speed += MOVE_INCREMENT


