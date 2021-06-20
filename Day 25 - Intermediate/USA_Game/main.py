import turtle
import pandas

screen = turtle.Screen()
screen.title('Name The States')
screen.setup(725, 491)
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
states_guessed = 0
already_guessed = []

game_is_on = True
draw = turtle.Turtle()
draw.hideturtle()
draw.penup()

data = pandas.read_csv('50_states.csv')

while game_is_on:
    answer_state = screen.textinput(
        title="States",
        prompt=f"{states_guessed}/{len(data.state)} States | What's another state name?"
        ).title()
    if answer_state == 'Exit':
        game_is_on = False

    elif answer_state in data.state.to_list() and answer_state not in already_guessed:
        states_guessed += 1
        already_guessed.append(answer_state)
        state = data[data.state == answer_state]
        draw.goto(int(state.x), int(state.y))
        draw.write(answer_state, align='center', font=('Arial', 8, 'normal'))

    if states_guessed == len(data.state):
        print('YOU WIN! You named all the states!')
        game_is_on = False

states_not_guessed = []
for state in data.state:
    if state not in already_guessed:
        states_not_guessed.append(state)

data_dict = {
    'Missing States': states_not_guessed
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv('states_to_learn.csv')
