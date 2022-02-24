print('Welcome to the Tic Tac Toe game!'.title())
print('Player 1: X')
print('Player 2: O')
print('''Here are the numbers for each space in the 3x3 grid:
 1 | 2 | 3 
-----------
 4 | 5 | 6 
-----------
 7 | 8 | 9 
''')
current_grid_list = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
grid_spaces = {'1': (0, 0), '2': (0, 1), '3': (0, 2), '4': (1, 0), '5': (1, 1), '6': (1, 2), '7': (2, 0), '8': (2, 1), '9': (2, 2)}
current_grid = f'''
 {current_grid_list[0][0]} | {current_grid_list[0][1]} | {current_grid_list[0][2]}
-----------
 {current_grid_list[1][0]} | {current_grid_list[1][1]} | {current_grid_list[1][2]}
-----------
 {current_grid_list[2][0]} | {current_grid_list[2][1]} | {current_grid_list[2][2]}
'''
current_player = 'X'


def check_win():  # https://lemmoscripts.com/wp/wp-content/uploads/2018/09/winning-combinations-005.svg
    players = ['X', 'O']
    for player in players:
        if current_grid_list[0][0] == player:  # Horizontal Top Row
            if current_grid_list[0][1] == player:
                if current_grid_list[0][2] == player:
                    return True, player

        if current_grid_list[1][0] == player:  # Horizontal Middle Row
            if current_grid_list[1][1] == player:
                if current_grid_list[1][2] == player:
                    return True, player

        if current_grid_list[2][0] == player:  # Horizontal Bottom Row
            if current_grid_list[2][1] == player:
                if current_grid_list[2][2] == player:
                    return True, player

        if current_grid_list[0][0] == player:  # Vertical Left Side Row
            if current_grid_list[1][0] == player:
                if current_grid_list[2][0] == player:
                    return True, player

        if current_grid_list[0][1] == player:  # Vertical Middle Row
            if current_grid_list[1][1] == player:
                if current_grid_list[2][1] == player:
                    return True, player

        if current_grid_list[0][2] == player:  # Vertical Right Side Row
            if current_grid_list[1][2] == player:
                if current_grid_list[2][2] == player:
                    return True, player

        if current_grid_list[0][0] == player:  # Diagonal Left To Right
            if current_grid_list[1][1] == player:
                if current_grid_list[2][2] == player:
                    return True, player

        if current_grid_list[0][2] == player:  # Diagonal Right To Left
            if current_grid_list[1][1] == player:
                if current_grid_list[2][0] == player:
                    return True, player
    return False


def update_grid():
    global current_grid
    current_grid = f'''
 {current_grid_list[0][0]} | {current_grid_list[0][1]} | {current_grid_list[0][2]}
-----------
 {current_grid_list[1][0]} | {current_grid_list[1][1]} | {current_grid_list[1][2]}
-----------
 {current_grid_list[2][0]} | {current_grid_list[2][1]} | {current_grid_list[2][2]}
'''


def move(um):
    um_tuple = grid_spaces[str(um)]
    if current_grid_list[um_tuple[0]][um_tuple[1]] == ' ':
        current_grid_list[um_tuple[0]][um_tuple[1]] = current_player
        next_player()
        update_grid()
        return False
    return True


def next_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


def get_user_move():
    while True:
        usr_move = input(f'{"Player 1" if current_player == "X" else "Player 2"} - Enter a number from 1 to 9: ')
        try:
            usr_move = int(usr_move)
            if 1 <= usr_move <= 9:
                break
            else:
                print('InvalidOptionError: Make sure you pick a number between 1 and 9. Try Again...')
        except ValueError:
            print('ValueError: You did not enter a number! Try Again...')
    return usr_move


def check_tie():
    for row in current_grid_list:
        for space in row:
            if space == " ":
                return False
    return True


def reset_game():
    global current_player, current_grid_list, current_grid
    current_grid_list = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    current_grid = f'''
 {current_grid_list[0][0]} | {current_grid_list[0][1]} | {current_grid_list[0][2]}
-----------
 {current_grid_list[1][0]} | {current_grid_list[1][1]} | {current_grid_list[1][2]}
-----------
 {current_grid_list[2][0]} | {current_grid_list[2][1]} | {current_grid_list[2][2]}
'''
    current_player = 'X'


running = True
while running:
    print('-' * 30)
    print(current_grid)
    space_already_taken = move(get_user_move())
    while space_already_taken:
        print('SpaceTakenError: That Space Has Already been taken! Try again...')
        space_already_taken = move(get_user_move())
    winner = check_win()

    if check_tie() or winner:
        if check_tie():
            print("Its A Tie!")
        if winner:
            print(current_grid)
            print(f"{'Player 1 Wins!' if winner[1] == 'X' else 'Player 2 Wins!'}")
            print('-' * 3)
        again = input('Would you like you play again? (Y/N): ')
        if again.lower() == 'y':
            running = True
            reset_game()
        else:
            running = False
            print('Thank you for playing!')
