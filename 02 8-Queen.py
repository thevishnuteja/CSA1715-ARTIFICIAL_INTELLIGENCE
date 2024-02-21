def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_queens(board, row, n, solutions):
    if row == n:
        solutions.append(board[:])  # Found a solution, copy the board
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_queens(board, row + 1, n, solutions)

def print_solution(solution):
    for row in solution:
        print(" ".join(["Q" if col == row else "." for col in range(len(solution))]))
    print()

if __name__ == "__main__":
    n = 8  # Change this value for an n x n board
    empty_board = [-1] * n
    solutions = []

    solve_queens(empty_board, 0, n, solutions)

    if solutions:
        print(f"Found {len(solutions)} solution(s) for {n}-Queens problem:")
        for idx, solution in enumerate(solutions):
            print(f"Solution {idx + 1}:")
            print_solution(solution)
    else:
        print(f"No solution found for {n}-Queens problem.")
