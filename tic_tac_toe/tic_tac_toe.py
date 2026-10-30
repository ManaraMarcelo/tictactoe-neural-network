# Tic Tac Toe game logic
from tic_tac_toe import constants as const

# Function to start the game
def start_game(board):
    print("Welcome to Tic Tac Toe!")
    # Choose game mode
    mode_game = input("Choose game mode:\n1. Player vs Player\n2. Player vs AI\nEnter 1 or 2: ")
    
    # Validate input
    if mode_game not in ['1', '2']:
        print("Invalid choice. Please enter 1 or 2.")
        return start_game(board)
    
    return mode_game

# Function to print the game board
def print_board(board=None):
    print(f"""
   1   2   3
A  {board[0]} | {board[1]} | {board[2]}
  ---+---+---
B  {board[3]} | {board[4]} | {board[5]}
  ---+---+---
C  {board[6]} | {board[7]} | {board[8]}
""")

# Function to get player choices
def get_player_choice():
    player_1 = input("Enter name for Player 1 (X | O): ")
    player_1 = player_1.strip().upper()
    # Ensure player 1 chooses a valid symbol
    
    # Validate input
    if player_1 not in [const.PLAYER_X, const.PLAYER_O]:
        print("Invalid choice. Please choose 'X' or 'O'.")
        return get_player_choice()
    
    # Assign the other symbol to player 2
    player_2 = const.PLAYER_O if player_1 == const.PLAYER_X else const.PLAYER_X
    print(f"Player 1 is '{player_1}' and Player 2 is '{player_2}'")
    return player_1, player_2

# Function to get a player's move
def get_move(player):
    move = input(f"Player {player}, enter your move (e.g., A1, B2): ")
    # Validate input
    return move.strip().upper()

# Function to update the board with a player's move
def update_board(board, move, player):
    mapping = const.MAPPING
    # Validate move
    if move in mapping and board[mapping[move]] == ' ':
        board[mapping[move]] = player
        return True
    else:
        print("Invalid move. Try again.")
        return False

# Function to check for a winner or tie
def check_winner(board):
    winning_combinations = const.WINNING_COMBINATIONS
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return board[combo[0]]
    if ' ' not in board:
        return 'Tie'
    return None
