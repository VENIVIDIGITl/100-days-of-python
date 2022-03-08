import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("U.S. States Game")
screen.bgcolor("#2c3e50")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < len(all_states):
    answer_state = screen.textinput(title=f"{len(guessed_states)} / {len(all_states)} States Correct. Keep Guessing...",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        # Create states_to_learn.csv
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        # Get x and y coordinates from the row of answer_state
        state_data = data[data.state == answer_state]
        x = int(state_data.x)
        y = int(state_data.y)
        # Write the state name on the map
        new_state = turtle.Turtle()
        new_state.hideturtle()
        new_state.penup()
        new_state.goto(x, y)
        new_state.write(answer_state, font=('Arial', 12, 'normal'))
