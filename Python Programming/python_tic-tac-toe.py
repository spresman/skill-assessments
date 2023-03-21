import time

board = [[0, 1, 2],
         [3, 4, 5],
         [6, 7, 8]
         ]


def board_print():
    print('\n')
    for i in range(3):
        if i == 1 or i == 2:
            print("----------")
        print(str(board[i][0]) + " | " + str(board[i][1]) + " | " + str(board[i][2]))
    print('\n')


def all_elements_same(lst):
    return all(x == lst[0] for x in lst)


def win():
    for i in range(3):
        if all_elements_same(board[i]) or all_elements_same([row[i] for row in board]):
            return True

    diag1 = [board[0][0], board[1][1], board[2][2]]
    diag2 = [board[0][2], board[1][1], board[2][0]]

    if all_elements_same(diag1) or all_elements_same(diag2):
        return True

    return False


def tie():
    for i in range(3):
        for j in range(3):
            if type(board[i][j]) == int:
                return False

    return True


def prompt():
    while True:
        player = input('Please either pick X or O: ').upper()

        if player != 'X' and player != 'O':
            print('Please pick either X or O.')
        else:
            break

    return player


def player_turn():
    while True:
        symbol = input("Choose an index from 0 to 8 on the board: ")

        if symbol.isdigit() and int(symbol) in range(9):
            index = int(symbol)
            if board[index // 3][index % 3] in range(9):
                break
            else:
                print('Pick another position.')
        else:
            print('Please pick an input between 0 and 8 from available squares.')

    return index


def my_turn():
    for i in range(3):
        for j in range(3):
            if type(board[i][j]) == int:
                return i * 3 + j

    return None


def play():
    print("Let's play tic-tac-toe!")

    player = prompt()

    # Initial state
    board_print()

    while True:

        if player == 'X':
            me = 'O'
            index = player_turn()
            board[index // 3][index % 3] = player

            board_print()

            if win():
                print('You win!!!!')
                break

            if tie():
                print("It's a tie! Try again!")
                break

            print('\nMy move...')

            time.sleep(1)

            my_index = my_turn()
            board[my_index // 3][my_index % 3] = me

            board_print()

            if win():
                print('You lost :( Better luck next time!')
                break

            if tie():
                print("It's a tie! Try again!")
                break



        elif player == 'O':

            me = 'X'
            my_index = my_turn()
            board[my_index // 3][my_index % 3] = me

            print('\nMy move...')

            time.sleep(1)

            board_print()

            if win():
                print('You lost :( Better luck next time!')
                break

            if tie():
                print("It's a tie! Try again!")
                break

            index = player_turn()
            board[index // 3][index % 3] = player

            board_print()

            if win():
                print('You win!!!!')
                break

            if tie():
                print("It's a tie! Try again!")
                break


play()
