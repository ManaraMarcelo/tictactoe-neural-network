# Run game file
from tic_tac_toe import constants as const
from tic_tac_toe import tic_tac_toe as ttt

# Initialize the game
def runGame(get_ai_move = None):
    # Initialize a new game board
    board = const.NEW_BOARD.copy()

    # Start the game
    mode_game = ttt.start_game(board)

    # For now, only Player vs Player is implemented
    if mode_game == '2':
        print("Your Player 2 is our implemented AI.")
    
    # Print the board
    ttt.print_board(board)

    # Get player names and symbols
    player1, player2 = ttt.get_player_choice()

    # Set the current player to player1
    current_player = player1

    while True:
        # Display the board
        ttt.print_board(board)
        
        # Get move as mode_game chose from Player
        if mode_game == '1' or current_player == player1:
            # Get the current player's move
            move = ttt.get_move(current_player)
        else:
            move = get_ai_move(board, current_player)
        
        # Update the board with the move
        if ttt.update_board(board, move, current_player):
            # Check for a winner or tie
            winner = ttt.check_winner(board)
            # If there's a winner or tie, end the game
            if winner:
                ttt.print_board(board)
                if winner == 'Tie':
                    print("It's a tie!")
                else:
                    print(f"Player {winner} wins!")
                break
            # Switch to the other player
            current_player = player2 if current_player == player1 else player1
        else:
            # Invalid move, ask the player to try again
            print("Please try again.")