def start():
    print('Welcome to Tic Tac Toe!')


def clear_board():
    for i in range(1, 10):
        board_map[i] = ''


def display_board(board):
    print(f'  {board[7]}  |  {board[8]}  | {board[9]}  ')
    print(f'---------------')
    print(f'  {board[4]}  |  {board[5]}  | {board[6]}  ')
    print(f'---------------')
    print(f'  {board[1]}  |  {board[2]}  | {board[3]}  ')


def player_mark(player):
    while True:
        position = int(input('Choose you position: (1-9) '))
        if position in range(1, 10) and board_map[position] == "":
            board_map[position] = player
            break
        else:
            print('Wrong position. Please try again.')


def first_player():
    while True:
        first_mark = input('Player 1: Do you want to be X or 0? ').upper()
        if first_mark == "X" or first_mark == "0":
            print('Player 1 will go first.')
            return first_mark
        else:
            print("Wrong mark. Please try again.")


def ready_to_play():
    while True:
        ready = input('Are You ready to play? Enter YES or NO. ').upper()
        if ready == 'YES':
            return True
        elif ready == 'NO':
            print('Thanks for You game')
            return False
        else:
            print('Unkown answer. Please try again.')


def play_again():
    while True:
        again = input('Do You want play again? Enter: Yes or No. ').upper()
        if again == 'YES':
            clear_board()
            return True
        elif again == 'NO':
            print('Thanks for You game')
            return False
        else:
            print('Unkown answer. Please try again.')


def check(board):
    if board_map[7] == board[8] == board[9] != "":
        print('You win game')
        return True
    elif board[4] == board[5] == board[6] != "":
        print('You win game')
        return True
    elif board[1] == board[2] == board[3] != "":
        print('You win game')
        return True
    elif board[7] == board[4] == board[1] != "":
        print('You win game')
        return True
    elif board[8] == board[5] == board[2] != "":
        print('You win game')
        return True
    elif board[9] == board[6] == board[3] != "":
        print('You win game')
        return True
    elif board[7] == board[5] == board[3] != "":
        print('You win game')
        return True
    elif board_map[1] == board[5] == board[9] != "":
        print('You win game')
        return True
    else:
        if "" in board.values():
            return False
        else:
            print('DRAW!')
            return True


while True:
    board_map = {7: "", 8: "", 9: "",
                 4: "", 5: "", 6: "",
                 1: "", 2: "", 3: ""}

    start()

    player_1 = first_player()
    if player_1 == "X":
        player_2 = "0"
    else:
        player_2 = 'X'

    play = ready_to_play()
    display_board(board_map)

    while play:

        player_mark(player_1)
        display_board(board_map)
        if check(board_map):
            break

        player_mark(player_2)
        display_board(board_map)
        if check(board_map):
            break

    if not play_again():
        break
