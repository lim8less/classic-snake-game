from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        super().shape("circle")
        super().penup()
        super().color("blue")
        super().speed("fastest")
        super().shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.refresh()

    def refresh(self):
        random_x = float(random.randint(-280, 280))
        random_y = float(random.randint(-280, 280))
        super().goto(random_x, random_y)
