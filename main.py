import random



def is_safe(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True



def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None



def generate_sudoku(difficulty):
    sudoku = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(0, 9, 3):
        fill_diagonal_box(sudoku, i, i)
    solve_sudoku(sudoku)

    # Remove cells to create the puzzle based on the chosen difficulty
    cells_to_remove = 81 - difficulty
    while cells_to_remove > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if sudoku[row][col] != 0:
            sudoku[row][col] = 0
            cells_to_remove -= 1

    return sudoku


def fill_diagonal_box(board, row, col):
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(num_list)
    idx = 0
    for i in range(3):
        for j in range(3):
            board[row + i][col + j] = num_list[idx]
            idx += 1


def solve_sudoku(board):
    row, col = find_empty_cell(board)
    if row is None and col is None:
        return True
    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False


def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))


def get_yes_or_no(prompt):
    while True:
        response = input(prompt).lower()
        if response == "yes" or response == "y":
            return True
        elif response == "no" or response == "n":
            return False
        else:
            print("Please enter 'yes' or 'no'.")


def get_integer(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_user_sudoku():
    sudoku = [[0 for _ in range(9)] for _ in range(9)]
    print("Enter your Sudoku puzzle:")
    for i in range(9):
        for j in range(9):
            prompt = f"Row {i + 1}, Column {j + 1} (0 for empty cell): "
            sudoku[i][j] = get_integer(prompt, 0, 9)
    return sudoku


def choose_difficulty():
    print("Choose difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    while True:
        choice = get_integer("Enter the number corresponding to the difficulty level: ", 1, 3)
        if choice == 1:
            return 35  # Number of cells to be filled in for easy difficulty
        elif choice == 2:
            return 25  # Number of cells to be filled in for medium difficulty
        elif choice == 3:
            return 20  # Number of cells to be filled in for hard difficulty
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def play_again():
    return get_yes_or_no("Do you want to play again? (yes/no): ")


def main():
    print("Welcome to Sudoku Solver!")

    while True:
        print("Options:")
        print("1. Generate a new Sudoku puzzle")
        print("2. Enter your own Sudoku puzzle")
        print("3. Quit")
        choice = get_integer("Enter the number corresponding to your choice: ", 1, 3)

        if choice == 1:
            difficulty = choose_difficulty()
            sudoku_puzzle = generate_sudoku(difficulty)
        elif choice == 2:
            sudoku_puzzle = get_user_sudoku()
        else:
            print("Thank you for using Sudoku Solver. Have a great day!")
            break

        print("\nSudoku puzzle:")
        print_board(sudoku_puzzle)

        solve = get_yes_or_no("Do you want to solve this Sudoku puzzle? (yes/no): ")
        if solve:
            if solve_sudoku(sudoku_puzzle):
                print("\nSudoku solved:")
                print_board(sudoku_puzzle)
            else:
                print("\nNo solution exists for the given Sudoku puzzle.")
        else:
            print("Sudoku puzzle not solved.")

        if not play_again():
            print("Thank you for using Sudoku Solver. Have a great day!")
            break


if __name__ == "__main__":
    main()
