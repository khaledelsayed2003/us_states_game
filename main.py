import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
background_image = "us_states_game/blank_states_img.gif"
screen.addshape(background_image) # to make it available for screen.
turtle.shape(background_image)


NUM_OF_CORRECT_STATES = 0
all_data = pd.read_csv("us_states_game/50_states.csv")
states_list = all_data.state.to_list()  # convert to normal Python list
ALL_STATES = len(states_list)
CORRECT_GUESS = []



game_is_on = True
while game_is_on:
    user_guess = screen.textinput(title=f"{NUM_OF_CORRECT_STATES}/{ALL_STATES} States Correct", prompt="What's another state name?").title()
    
    if user_guess in states_list:
        if user_guess in CORRECT_GUESS:
            continue
        guess_coor_row = all_data[all_data.state == user_guess]
        x_coor = float(guess_coor_row.x)
        y_coor = float(guess_coor_row.y)
        new_state = turtle.Turtle()
        new_state.penup()
        new_state.hideturtle()
        new_state.goto(x_coor, y_coor)
        new_state.write(user_guess)
        NUM_OF_CORRECT_STATES += 1
        CORRECT_GUESS.append(user_guess)
        






































screen.exitonclick()







