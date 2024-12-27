import os
from colorama import Fore, Style, init   #imports colorama package for coloring the font

# Initialize colorama
init()

# print the Tic-Tac-Toe board
def print_board(board): 
    print("-------------")
    print("| " + color_text(board[0]) + " | " + color_text(board[1]) + " | " + color_text(board[2]) + " |")
    print("-------------")
    print("| " + color_text(board[3]) + " | " + color_text(board[4]) + " | " + color_text(board[5]) + " |")
    print("-------------")
    print("| " + color_text(board[6]) + " | " + color_text(board[7]) + " | " + color_text(board[8]) + " |")
    print("-------------")

# color the text based on the player's symbol
def color_text(text):
    if text == 'X':
        return Fore.RED + text + Style.RESET_ALL
    elif text == 'O':
        return Fore.BLUE + text + Style.RESET_ALL
    else:
        return text

# player's move 
def player_move(board, player_symbol):
    while True:
        try:
            # Prompt player to choose a position
            choice = int(input(f"Player {player_symbol}, choose a position (1-9): "))
            # Check if the chosen position is between 1-9 and empty
            if 1 <= choice <= 9 and board[choice - 1] not in ['X', 'O']:
                board[choice - 1] = player_symbol # choice-1 makes the index 0-8 instead of 1-9 so it is easier to add
                return board
            else:
                print("Invalid input. Please choose an empty position.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# check if there is a winner
def check_win(board):
    win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6))
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] in ['X', 'O']:
            return combo, board[combo[0]]
    return None, None

# Main function to play the game
def play_game():
    player1_wins = 0
    player2_wins = 0
    
    while True:
        # make the board with the numbers
        # this array will show the possible moves that a player can make via numbers left on the board
        
        board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        current_player = 'X'

        while True:
            # Clear the screen for every turn
            os.system('cls' if os.name == 'nt' else 'clear')
            print("  --- Tic-Tac-Toe ---  ")
            print(f"  Current Turn: Player {current_player}  ")
            print_board(board) # prints the current move updated 

            # prompts for an X or O depending on the current_player
            board = player_move(board, current_player)

            # Check for a winner
            winning_combo, winner = check_win(board) #checking the board for a winning combonation
            if winner:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("  --- Tic-Tac-Toe ---  ")
                print(f"  Current Turn: Player {current_player}  ")
                print_board(board)
                print(f"Player {winner} wins!")
                if winner == 'X':      #if winning combo, check that winner is X then X wins if not O wins. Then add 1 to their winning total
                    player1_wins += 1
                else:
                    player2_wins += 1
                break

            # Check for a tie
            if all(cell in ['X', 'O'] for cell in board): #all function checks the index to see if it is filled and if there is no winning combonation it's a tie
                os.system('cls' if os.name == 'nt' else 'clear')
                print("  --- Tic-Tac-Toe ---  ")
                print(f"  Current Turn: Player {current_player}  ")
                print_board(board)
                print("It's a tie!")
                break

            # Switch player
            current_player = 'O' if current_player == 'X' else 'X'

        # Print the score
        print("\nScore:")
        print(f"Player 1 (X): {player1_wins}")
        print(f"Player 2 (O): {player2_wins}")

        # Ask if players want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

# play game
if __name__ == "__main__":
    play_game()
