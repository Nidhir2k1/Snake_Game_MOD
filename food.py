from turtle import Turtle
import random
food_shape=("circle","turtle","arrow")
class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed(0)
        self.refresh()

    def refresh(self):
        random_x=random.randint(-250,250)
        random_y=random.randint(-250,250)
        self.goto(random_x,random_y)