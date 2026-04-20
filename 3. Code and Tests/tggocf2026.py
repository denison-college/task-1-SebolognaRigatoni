import numpy as np
board = None
columns = 0
rows = 0

# create players
player = {
    1: {'name': '', 'score': 100, 'piece': '●', 'finalScore': 0},
    2: {'name': '', 'score': 100, 'piece': '■', 'finalScore': 0}
    }
while True:
    player[1]['name'] = input("What is player 1's 4 letter name?").upper()
    if len(player[1]['name']) != 4 or not (player[1]['name'].isalpha()):
        print('4 alphabet letters please.')
    else:
        break
while True:
    player[2]['name'] = input("What is player 2's 4 letter name?").upper()
    if len(player[2]['name']) != 4 or not (player[2]['name'].isalpha()):
        print('4 alphabet letters please.')
    if player[2]['name'] == player[1]['name']:
        print('Names cannot be the same.')
    else:
        break
# generate game board
def generate_board():
    global board, rows, columns
    rows = 6
    columns = 7
    board = np.full((rows, columns), '◯')
    return board
generate_board()
def checkwin():
    global winDirection
    # check horizontal
    for row in range(rows):
        for column in range(columns - 3):
            if board[row][column] in ('●', '■'):
                if board[row][column] == board[row][column + 1] == board[row][column + 2] == board[row][column + 3]:
                    winDirection = 'horizontally'
                    return True
    # check vertical
    for column in range(columns):
        for row in range(rows - 3):
            if board[row][column] in ('●', '■'):
                if board[row][column] == board[row + 1][column] == board[row + 2][column] == board[row + 3][column]:
                    winDirection = 'vertically'
                    return True
    # check diagonal positive
    for column in range(columns):
        for row in range(rows - 3):
            if board[row][column] in ('●', '■'):
                if board[row][column] == board[row + 1][column+1] == board[row + 2][column+2] == board[row + 3][column+3]:
                    winDirection = 'diagonally'
                    return True
# check diagonal negative
    for column in range(columns):
        for row in range(rows - 3):
            if board[row][column] in ('●', '■'):
                if board[row][column] == board[row + 1][column-1] == board[row + 2][column-2] == board[row + 3][column-3]:
                    winDirection = 'diagonally'
                    return True

def playgame():
    global player
    gaming = True
    while gaming:
        for i in player:
            print(board)
            print(f"{player[i]['name']}'s turn")
            column = int(input(f'Select column 1 to {columns}')) - 1
            # check column from bottom to top, drop if empty
            full = True
            for row in range(rows - 1, -1, -1):
                if board[row][column] == '◯':
                    board[row][column] = f'{player[i]['piece']}'
                    full = False
                    break
            if full:
                print('Column Full')
            if checkwin():
                player[i]['finalScore'] = player[i]['score']
                print(f'{player[i]['name']} wins {winDirection} with {player[i]['finalScore']} points left!')
                print(board)
                gaming = False
                break
            # if they havent placed the winning piece, subtract points.
            # not sure if i should subtract points when they place the winning piece
            # i think not
            player[i]['score'] -= 2

playgame()
print('Game Over')
