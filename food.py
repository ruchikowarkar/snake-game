from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed("fastest")

    def drop_food(self):
        x_position = 20 * random.randint(-14, 14)
        y_position = 20 * random.randint(-14, 14)
        self.setx(x_position)
        self.sety(y_position)
