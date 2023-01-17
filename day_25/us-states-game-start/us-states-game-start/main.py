import turtle
import pandas

data = pandas.read_csv("50_states.csv")

list_of_states = data.state.tolist()
print(list_of_states)

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
t = turtle.Turtle()
t.penup()
t.hideturtle()
correct_guess = []

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f'{len(correct_guess)}/{len(list_of_states)} States Correct',
                                    prompt="What's another state's name?")
    user_state = answer_state.title()
    # for exit the game type exit
    if user_state == 'Exit':
        break
    # retrieve co-ordinates of the state entered
    if user_state in list_of_states and user_state not in correct_guess:
        row = data[data.state == user_state]
        row_data = row.values.tolist()
        x = row_data[0][1]
        y = row_data[0][2]
        # other option are row.x we can use
        name = row_data[0][0]
        # showing names in the correct coordinates in the map
        t.goto(x, y)
        # this item will give only value
        t.write(row.state.item())
        correct_guess.append(user_state)
        if len(correct_guess) == 50:
            game_is_on = False


# creating the csv file to show what are the states are guessed correctly
df = pandas.DataFrame(correct_guess)
df.to_csv("guessed_state.csv")
