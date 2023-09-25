from turtle import Turtle


class Name(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.hideturtle()
        self.color("Black")

    def show_state(self, coordinates, name):
        self.goto(coordinates)
        self.write(f"{name}")
