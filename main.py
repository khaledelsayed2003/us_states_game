import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
background_image = "us_states_game/blank_states_img.gif"
screen.addshape(background_image) # to make it available for screen.
turtle.shape(background_image)


num_of_correct_guesses = 0
all_data = pd.read_csv("us_states_game/50_states.csv")
states_list = all_data.state.to_list()  # convert to normal Python list
states_length = len(states_list)
correct_guessed_list = []
x_axis_list = []
y_axis_list = []




game_is_on = True
while game_is_on:
    user_guess = screen.textinput(title=f"{num_of_correct_guesses}/{states_length} States Correct", prompt="What's another state name?\n(Type 'Exit' to quit the game)").title()

    if user_guess == "Exit":
        game_is_on = False
        # creating a csv file to save the states that user have guessed.
        guessed_states = {
            "state": correct_guessed_list,
            "x" : x_axis_list,
            "y" : y_axis_list
        }
        guessed_states_file = pd.DataFrame(guessed_states)
        guessed_states_file.to_csv("us_states_game/guessed_states_file.csv")
        
        # creating a csv file to save the states that user have not guessed.
        missing_states = [state for state in states_list if state not in correct_guessed_list]  #updated to use list comprehension.
        unguessed_states = {
            "missed_state" : missing_states
        }
        ungessed_states_file = pd.DataFrame(unguessed_states)
        ungessed_states_file.to_csv("us_states_game/unguessed_states_file.csv")
                
    
    if user_guess in states_list:
        if user_guess in correct_guessed_list:
            continue
        guess_coor_row = all_data[all_data.state == user_guess]
        x_coor = float(guess_coor_row.x) # we have to convert the coor because the value in csv files are always str.
        y_coor = float(guess_coor_row.y)
        new_state = turtle.Turtle()
        new_state.penup()
        new_state.hideturtle()
        new_state.goto(x_coor, y_coor)
        new_state.write(user_guess)
        num_of_correct_guesses += 1
        correct_guessed_list.append(user_guess)
        x_axis_list.append(x_coor)
        y_axis_list.append(y_coor)
        if correct_guessed_list == states_list:
            game_is_on = False


# screen.exitonclick()   # we deleted this method in order to make the window exits by itself when we type Exit.







