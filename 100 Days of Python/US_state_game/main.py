import turtle
from state_name import Name
import pandas as pd

data = pd.read_csv("50_states.csv")
state_list = list(data.state)
states_data = {}

for j in range(len(state_list)):
    state_name = state_list[j].lower()
    coordinates = (data.x[j], data.y[j])
    states_data[state_name] = coordinates

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

show_state = Name()

states_guessed = 0
guessed_list = []

while states_guessed < 50:
    answer = turtle.textinput(f"{states_guessed}/50 States Correct", "What's another state name?").lower()

    if answer in states_data and answer not in guessed_list:
        guessed_list.append(answer)
        states_guessed += 1
        coordinates = states_data[answer]
        show_state.show_state(coordinates, answer.capitalize())

turtle.mainloop()
