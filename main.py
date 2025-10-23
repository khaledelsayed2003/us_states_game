import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
background_image = "us_states_game/blank_states_img.gif"
screen.addshape(background_image) # to make it available for screen.
turtle.shape(background_image)


NUM_OF_CORRECT_STATES = 0
all_data = pd.read_csv("us_states_game/50_states.csv")
states_list = all_data.state
ALL_STATES = len(states_list)



user_guess = screen.textinput(title=f"{NUM_OF_CORRECT_STATES}/{ALL_STATES} States Correct", prompt="What's another state name?")











































screen.exitonclick()







