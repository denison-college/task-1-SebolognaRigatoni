import numpy as np
board = None
columns = 0
rows = 0
# generate game board
def generate_board():
    global board, rows, columns
    rows = int(input('Rows:'))
    columns = int(input('Columns:'))
    board = np.full((rows, columns), '◯')
    return board
generate_board()
def checkwin():
    # check horizontal
    for row in range(rows):
        for column in range(columns - 3):
            if board[row][column] in ('●', '■'):
                if board[row][column] == board[row][column + 1] == board[row][column + 2] == board[row][column + 3]:
                    print('Player', str(board[row][column])[0], 'wins!')
                    return True
    # check vertical
    for column in range(columns):
        for row in range(rows - 3):
            if board[row][column] in ('●', '■'):
                if board[row][column] == board[row + 1][column] == board[row + 2][column] == board[row + 3][column]:
                    print('Player', str(board[row][column])[0], 'wins!')
                    return True
    # check diagonal positive
    for column in range(columns):
        for row in range(rows - 3):
            if board[row][column] in ('●', '■'):
                if board[row][column] == board[row + 1][column+1] == board[row + 2][column+2] == board[row + 3][column+3]:
                    print('Player', str(board[row][column])[0], 'wins!')
                    return True
# check diagonal negative
    for column in range(columns):
        for row in range(rows - 3):
            if board[row][column] in ('●', '■'):
                if board[row][column] == board[row + 1][column-1] == board[row + 2][column-2] == board[row + 3][column-3]:
                    print('Player', str(board[row][column])[0], 'wins!')
                    return True

def playgame():
    player1 = True
    while True:
        print(board)
        if player1:
            playerPiece = '●'
            player1 = False
        else:
            playerPiece = '■'
            player1 = True
        print(f'{playerPiece} turn')
        column = int(input(f'Select column 1 to {columns}')) - 1
        # check column from bottom to top, drop if empty
        full = True
        for row in range(rows - 1, -1, -1):
            if board[row][column] == '◯':
                board[row][column] = playerPiece
                full = False
                break
        if full:
            print('Column Full')
        if checkwin():
            print(board)
            break

playgame()
print('Game Over')