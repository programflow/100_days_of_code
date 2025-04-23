import turtle
from state_manager import StateManager
import pandas as pd
import time

TIMER = 180  # 3 minutes in seconds

timer_display = turtle.Turtle()
timer_display.hideturtle()
timer_display.penup()
timer_display.goto(-280, 260)  # top-left corner of screen


def countdown():
    global TIMER
    timer_display.clear()
    timer_display.write(f"Time: {TIMER}", align="left", font=("Courier", 16, "bold"))
    if TIMER > 0:
        TIMER -= 1
        screen.ontimer(countdown, 1000)  # run again in 1 second
    else:
        screen.bye()  # closes the window when time is up




screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
state_manager = StateManager()
turtle.shape(image)


# def get_mouse_click_coordinates(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coordinates)
state_data = pd.read_csv("50_states.csv")
game_on = True
countdown()
while game_on:
    states_guessed = len(state_manager.states_found)
    try:
        answer_state = screen.textinput(title = f"{states_guessed}/50 States Correct", prompt = "What's another state's name?").title()
    except AttributeError or None:
        print("Try a state name or exit!")
        answer_state = 0

    if answer_state == "Exit":
        break


    if state_manager.state_not_found(answer_state) and answer_state in state_data.state.unique():

        # turns specific row of data frame into a flat list
        state_series= state_data.loc[state_data.state == answer_state].values.flatten().tolist()
        state_name =state_series[0]
        state_x_coordinate = state_series[1]
        state_y_coordinate = state_series[2]
        state_manager.make_state(state_name, state_x_coordinate, state_y_coordinate)



    if state_manager.found_all_states():
        game_on = False

print(f"\n⏰ Time's up! You guessed {len(state_manager.states_found)}/50 states correctly.")
screen.bye()



states_list = state_data.state.unique().tolist()
states_to_learn = [state for state in states_list if state not in state_manager.states_found]

new_data = pd.DataFrame(states_to_learn)
new_data.to_csv("states_to_learn.csv", mode = "w", index = False)







