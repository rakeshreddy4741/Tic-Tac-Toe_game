import random
def display_board(board):
    # this display the board

    print('         |         |         ')
    print('   ' + board[7] + '     |    ' + board[8] + '    |    ' + board[9])
    print('         |         |         ')
    print('-----------------------------')
    print('         |         |         ')
    print('   ' + board[4] + '     |    ' + board[5] + '    |    ' + board[6])
    print('         |         |         ')
    print('-----------------------------')
    print('         |         |         ')
    print('   ' + board[1] + '     |    ' + board[2] + '    |    ' + board[3])
    print('         |         |         ')

def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O?').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def replay():
    replay_input = input("Do You want ro replay game (yes or no):").upper()
    if replay_input == "YES":
        return True
    elif replay_input == "NO":
        return False

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal

def space_check(board,position):
    return board[position] == " "

def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position
def full_board_check(board):
    for j in range(1, 10):
        if space_check(board, j):
            return False
    return True
board = ['#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
display_board(board)
print("Welcome to the Tic Tac Toe!")


while True:
    board = [' '] * 10
    player_1, player_2 = player_input()
    turn = choose_first()
    print(f"{turn} will play first")

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'Player 1':
            display_board(board)
            position = player_choice(board)
            place_marker(board,player_1,position)

            if win_check(board,player_1):
                display_board(board)
                print("Player 1 Win")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("draw")
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board, player_2, position)
            if win_check(board, player_2):
                display_board(board)
                print("Player 2 Win")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("draw")
                    break
                else:
                    turn = 'Player 1'

    if not replay():
<<<<<<< HEAD
        break
=======
        break                             # breaks if user doesn't want to play again
>>>>>>> a7cdbd2 (Initial commit)

























