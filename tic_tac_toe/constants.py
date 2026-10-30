PLAYER_X = 'X'
PLAYER_O = 'O'

NEW_BOARD = [' '] * 9

MAPPING = {
    'A1': 0, 'A2': 1, 'A3': 2,
    'B1': 3, 'B2': 4, 'B3': 5,
    'C1': 6, 'C2': 7, 'C3': 8
}

WINNING_COMBINATIONS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8], # columns
    [0, 4, 8], [2, 4, 6]             # diagonals
]