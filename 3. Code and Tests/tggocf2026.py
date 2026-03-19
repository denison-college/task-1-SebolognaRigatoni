import numpy as np
board = None
columns = 0
rows = 0
# generate game board
def generate_board():
    global board, rows, columns
    rows = int(input('Rows:'))
    try:
        rows = int(rows)
    except ValueError:
    # Handle error
        print('error')
    columns = int(input('Columns:'))

    try:
        columns = int(columns)
    except ValueError:
        print('error')

    board = np.full((rows, columns), '◯')
    return board
generate_board()
print(board)

def drop(player_piece):
    for row in range(rows - 1, -1, -1):
        if board[row][column] == '◯':
            board[row][column] = player_piece
            print(board)
            full = False
            break
    if full == True:
        print('Board Full')

def playgame():
    while True:
        column = int(input(f'Select column 1 to {columns}')) - 1
        # check column from bottom to top, drop if empty
        full = True

playgame()