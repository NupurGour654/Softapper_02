import os

# Scoreboard dictionary
score = {"X": 0, "O": 0, "Draw": 0}

def show_board_positions():
    print("\nBoard Positions (for reference):")
    positions = [[str(i + j * 3 + 1) for i in range(3)] for j in range(3)]
    for row in positions:
        print(" | ".join(row))
        print("-" * 6)
    print()

def print_board(board):
    print("\nCurrent Board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 6)
    print()
    print(f"Scoreboard: X - {score['X']}, O - {score['O']}, Draws - {score['Draw']}\n")

def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(all(cell != " " for cell in row) for row in board)

def get_move(player, board):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid move. Please enter a number between 1 and 9.")
                continue
            row, col = divmod(move - 1, 3)
            if board[row][col] != " ":
                print("Cell already occupied. Choose a different move.")
                continue
            return row, col
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def main():
    print(" Welcome to Tic Tac Toe!")
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = "X"
        show_board_positions()
        print_board(board)

        while True:
            row, col = get_move(current_player, board)
            board[row][col] = current_player
            os.system('cls' if os.name == 'nt' else 'clear')
            show_board_positions()
            print_board(board)

            if check_winner(board, current_player):
                print(f" Player {current_player} wins!\n")
                score[current_player] += 1
                break
            elif is_draw(board):
                print("It's a draw!\n")
                score["Draw"] += 1
                break

            current_player = "O" if current_player == "X" else "X"

        while True:
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again in ["yes", "no"]:
                break
            print("Please enter 'yes' or 'no'.")

        if play_again == "no":
            print("\nThanks for playing!")
            print(f" Final Scores: X - {score['X']}, O - {score['O']}, Draws - {score['Draw']}")
            break

if __name__ == "__main__":
    main()
