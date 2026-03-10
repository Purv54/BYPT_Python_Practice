board = [' ']*10

def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])

def player_input():
    marker = ''

    while  not (marker == 'X' or marker == 'O'):
        marker = input("Player1 choose X or O: ").upper()

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board, marker, position):

    board[position] = marker

def win_check(board, mark):

    return ((board[7] == board[8] == board[9] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[1] == board[2] == board[3] == mark) or
            (board[7] == board[4] == board[1] == mark) or
            (board[8] == board[5] == board[2] == mark) or
            (board[9] == board[6] == board[3] == mark) or
            (board[7] == board[5] == board[3] == mark) or
            (board[9] == board[5] == board[1] == mark))

def space_check(board, position):
    return board[position] == " "

def full_board(board):
      for i in range(1,10):
        if space_check(board,i):
           return False
      return True

def player_choice(board):
     position = 0
     while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
          position = int(input("enter a number between 1-9: "))

     return position

def replay():
    choice = input("do you want to play agian. Yes or No : ")

    return choice == "Yes" or choice == "yes"

import random

def choose_first():

    flip = random.randint(0,1)

    if flip == 0:
       return "Player1"
    else:
       return "Player2"
    
while True:

    board = [" "] * 10

    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + " will go first.")

    play_game = input("Do you want to play? Y or N: ").upper()

    while play_game != "Y" and play_game != "N":
        play_game = input("Do you want to play? Y or N: ").upper()
    
    if play_game == "N":
        break

    game_on = True

    while game_on:

        if turn == "Player1":

            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)

            if win_check(board, player1_marker):
                display_board(board)
                print("Player1 Won!")
                game_on = False

            elif full_board(board):
                display_board(board)
                print("It's a Tie!")
                game_on = False

            else:
                turn = "Player2"

        else:

            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)

            if win_check(board, player2_marker):
                display_board(board)
                print("Player2 Won!")
                game_on = False

            elif full_board(board):
                display_board(board)
                print("It's a Tie!")
                game_on = False

            else:
                turn = "Player1"
    
    if not replay():
        break
