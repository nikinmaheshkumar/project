import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board,mark):
    for row in board:
        if all(cell == mark for cell in row):
            return True
    for col in range(3):
        if all(row[col] == mark for row in board):
            return True
    if all(board[i][i] == mark for i in range(3)) or all(board[i][2-i] == mark for i in range(3)):
        return True
    return False

def get_empty_positions(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def computer_move(board):
    return random.choice(get_empty_positions(board))

def play_tic_tac_toe(mode="2p"):
    board = [ [" "]*3 for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        mark = players[turn % 2]
        print(f"Player {mark}'s turn")

        if mode == "1p" and mark == "O":
            row, col = computer_move(board)
        else:
            try:
                r, c = map(int, input("Enter row and column (0-2): ").split())
            except ValueError:
                print("Invalid input. Use two numbers from 0 to 2.")
                continue
                    if not (0 <= r <= 2 and 0 <= c <= 2):
            print("Coordinates out of range.")
            continue
