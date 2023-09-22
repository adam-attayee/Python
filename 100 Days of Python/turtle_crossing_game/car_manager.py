from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(self.starting_position())

    def drive(self, player_level):
        self.new_xcor = self.xcor() - (STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * player_level))
        self.goto(self.new_xcor, self.ycor())

    def starting_position(self):
        self.starting_xcor = random.randint(300, 1000)
        self.starting_ycor = random.randint(-250, 250)
        return self.starting_xcor, self.starting_ycor

    def reset_position(self):
        self.goto(self.starting_position())
