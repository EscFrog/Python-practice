from random import randint

board = []
initTurn = 4

for x in range(5):
    board.append(["O"] * 5)


def print_board(board):
    print("")
    for row in board:
        print(" ".join(row))


print("Let's play Battleship!")


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)


def play_round(left_turn):
    while left_turn > 0:
        print_board(board)
        print("Left turn = " + str(left_turn))
        try:
            guess_row = int(input("Guess Row:"))-1
            guess_col = int(input("Guess Col:"))-1
        except:
            print('please right number')
        else:
            if guess_row == ship_row and guess_col == ship_col:
                print("Congratulations! You sunk my battleship!")
                break
            else:
                if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                    print("Oops, that's not even in the ocean.")
                elif board[guess_row][guess_col] == "X":
                    print("You guessed that one already.")
                else:
                    print("You missed my battleship!")
                    board[guess_row][guess_col] = "X"
                    left_turn -= 1
    board[ship_row][ship_col] = "*"
    print_board(board)
    print("Game Over")
    print("The battleship is in " + str(ship_row + 1) + "," + str(ship_col + 1))

play_round(initTurn)
