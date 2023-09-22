from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto((-280, 260))
        self.level = 0
        self.score()

    def score(self):
        self.clear()
        self.write(f"Level: {self.level}", move=False, align='left', font=FONT)

    def level_up(self):
        self.level += 1

    def game_over(self):

        self.goto(-80, 0)
        self.write("Game Over!", move=False, align='left', font=FONT)
