from tkinter import *
from random import choice

FONT = ('Comic Sans MS', 12, 'normal')
choices = ['Rock', 'Paper', 'Scissors']
player_score = 0
computer_score = 0


def update_text(user_choice, computer_choice, winner):
    winner_text = ''
    if winner == 'player':
        winner_text = 'You Win!'
    elif winner == 'computer':
        winner_text = 'Computer Won!'
    elif winner == 'draw':
        winner_text = "It's a Draw!"
    text.delete('1.0', END)
    text.insert(END, f'''Your Choice: {user_choice}
Computer's Choice: {computer_choice}
------------------------------
{winner_text}
------------------------------
Your Score: {player_score}
Computer Score: {computer_score}''')


def increase_scores(who):
    global player_score
    global computer_score
    if who == 'player':
        player_score += 1
    elif who == 'computer':
        computer_score += 1


def rock():
    cpu = choice(choices)
    winner = ''
    if cpu == 'Rock':
        winner = 'draw'
    elif cpu == 'Paper':
        winner = 'computer'
        increase_scores('computer')
    elif cpu == 'Scissors':
        winner = 'player'
        increase_scores('player')
    update_text('Rock', cpu, winner)


def paper():
    cpu = choice(choices)
    winner = ''
    if cpu == 'Paper':
        winner = 'draw'
    elif cpu == 'Scissors':
        winner = 'computer'
        increase_scores('computer')
    elif cpu == 'Rock':
        winner = 'player'
        increase_scores('player')
    update_text('Paper', cpu, winner)


def scissors():
    cpu = choice(choices)
    winner = ''
    if cpu == 'Scissors':
        winner = 'draw'
    elif cpu == 'Rock':
        winner = 'computer'
        increase_scores('computer')
    elif cpu == 'Paper':
        winner = 'player'
        increase_scores('player')
    update_text('Scissors', cpu, winner)


window = Tk()
window.title('Rock, Paper, Scissors')
window.config(padx=20, pady=20)

# BUTTONS
rock_button = Button(text='Rock', command=rock, font=FONT, bg="#38c3f5")
rock_button.grid(row=1, column=0)
rock_button.config(width=6)

paper_button = Button(text='Paper', command=paper, font=FONT, bg='#fc627c')
paper_button.grid(row=1, column=1)
paper_button.config(width=6)

scissors_button = Button(text='Scissors', command=scissors, font=FONT, bg='#8bff61')
scissors_button.grid(row=1, column=2)
scissors_button.config(width=6)

# TEXT BOX
text = Text(master=window, height=7, width=30, bg="#FFFF99", font=FONT)
text.insert(END, 'Your turn to choose, click a button...')
text.grid(row=0, column=1)

window.mainloop()
