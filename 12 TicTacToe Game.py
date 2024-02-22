def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def print_result(board, player):
    print_board(board)
    if check_winner(board, player):
        print(f"Player {player} wins!")
    else:
        print("It's a tie!")

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn")
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter col (0-2): "))
            if row < 0 or row > 2 or col < 0 or col > 2:
                raise ValueError("Invalid input. Row and column must be between 0 and 2.")
        except ValueError as e:
            print(e)
            continue

        if board[row][col] != " ":
            print("Cell already occupied. Try again.")
            continue

        board[row][col] = player
        if check_winner(board, player) or is_board_full(board):
            print_result(board, player)
            break

        turn += 1

if __name__ == "__main__":
    tic_tac_toe()
