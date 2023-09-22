import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


game_is_on = True
player = Player()
scoreboard = Scoreboard()
screen.onkey(player.move, "Up")

cars = []
level = 0

for _ in range(15):
    new_car = CarManager()
    cars.append(new_car)


while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.score()

    for car in cars:
        car.drive(level)

    if player.ycor() >= 290:
        player.start_position()
        scoreboard.level_up()
        level += 1

    for car in cars:
        if car.xcor() < - 300:
            car.reset_position()
        elif car.distance(player.position()) < 15:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
