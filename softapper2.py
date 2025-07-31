def show_board_positions():
    print("\nBoard Positions:")
    positions = [[str(i + j * 3 + 1) for i in range(3)] for j in range(3)]
    for row in positions:
        print(" | ".join(row))
        print("-" * 6)
    print()


def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 6)
    print("\n")

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

def get_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid move. Please enter a number between 1 and 9.")
                continue
            row, col = divmod(move - 1, 3)
            return row, col
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def main():
    print("Welcome to Tic Tac Toe!")
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
print_board(board)

        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = "X"
        print_board(board)

        while True:
            row, col = get_move(current_player)
            if board[row][col] == " ":
                board[row][col] = current_player
                print_board(board)

                if check_winner(board, current_player):
                    print(f"Player {current_player} wins!")
                    break
                elif is_draw(board):
                    print("It's a draw!")
                    break
                current_player = "O" if current_player == "X" else "X"
            else:
                print("The cell is already occupied. Please choose a different move.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break   
        show_board_positions()

if __name__ == "__main__":
    main()



