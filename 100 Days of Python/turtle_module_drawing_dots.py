import turtle
import random

color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]

turtle.colormode(255)
tim = turtle.Turtle()
tim.hideturtle()

def set_position(reposition_y):
    x_coordinate = -250
    y_coordinate = -250 + reposition_y
    x_y_coordinate = (x_coordinate, y_coordinate)
    return x_y_coordinate


def paint_row():
    tim.speed(0)
    for _ in range(1, 11):
        tim.color(random.choice(color_list))
        tim.dot(20)
        tim.penup()
        tim.forward(50)


y = 0
for _ in range(1, 11):
    starting_position = set_position(y)
    tim.penup()
    tim.setpos(starting_position)
    paint_row()
    y += 50


screen = turtle.Screen()
screen.exitonclick()
