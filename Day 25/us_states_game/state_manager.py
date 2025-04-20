from turtle import Turtle

class StateManager(Turtle):
    def __init__(self):
        super().__init__()
        self.states_found =[]


    def make_state(self, state_name, x_cor, y_cor):
        self.hideturtle()
        self.penup()
        self.goto(x_cor, y_cor)
        self.write(state_name, align="center", font=("Arial", 14, "bold"))
        self.states_found.append(state_name)


    def state_not_found(self, state_name):
        return state_name not in self.states_found

    def found_all_states(self):
        return len(self.states_found) == 50
