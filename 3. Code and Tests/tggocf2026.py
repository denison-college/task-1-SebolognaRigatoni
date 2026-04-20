import numpy as np
import datetime
import pathlib
import time
import sys
import pygame
gameResults = ''
board = None
columns = 0
rows = 0
def slowprint(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0015)
# Pieces: '◯' for empty slot, '●' for p1, '■' for p2
# create players
player = {
    1: {'name': '', 'score': 100, 'piece': '●', 'finalScore': 0},
    2: {'name': '', 'score': 100, 'piece': '■', 'finalScore': 0}
    }
pygame.mixer.init()
intro = pygame.mixer.Sound('3. Code and Tests/intro.wav')
intro.play()
time.sleep(1)
slowprint('WELCOME TO\n')
time.sleep(2.5)
slowprint('THE BEST EXPERIENCE IN ALL OF PYTHON GAMING HISTORY\n')
time.sleep(2.5)
slowprint('AVAILABLE EXCLUSIVELY FOR BATHURST HIGH SOFTWARE ENGINEERING STUDENTS\n')
time.sleep(2.5)
slowprint('''


████████╗██╗  ██╗███████╗     ██████╗ ██████╗ ███████╗ █████╗ ████████╗███████╗███████╗████████╗     ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ███████╗    
╚══██╔══╝██║  ██║██╔════╝    ██╔════╝ ██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██╔════╝    
   ██║   ███████║█████╗      ██║  ███╗██████╔╝█████╗  ███████║   ██║   █████╗  ███████╗   ██║       ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║█████╗      
   ██║   ██╔══██║██╔══╝      ██║   ██║██╔══██╗██╔══╝  ██╔══██║   ██║   ██╔══╝  ╚════██║   ██║       ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║██╔══╝      
   ██║   ██║  ██║███████╗    ╚██████╔╝██║  ██║███████╗██║  ██║   ██║   ███████╗███████║   ██║       ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝██║         
   ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚══════╝   ╚═╝        ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝ ╚═╝         
                                                                                                                                                                 
 ██████╗ ██████╗ ███╗   ██╗███╗   ██╗███████╗ ██████╗████████╗    ███████╗ ██████╗ ██╗   ██╗██████╗     ██████╗  ██████╗ ██████╗  ██████╗                        
██╔════╝██╔═══██╗████╗  ██║████╗  ██║██╔════╝██╔════╝╚══██╔══╝    ██╔════╝██╔═══██╗██║   ██║██╔══██╗    ╚════██╗██╔═████╗╚════██╗██╔════╝                        
██║     ██║   ██║██╔██╗ ██║██╔██╗ ██║█████╗  ██║        ██║       █████╗  ██║   ██║██║   ██║██████╔╝     █████╔╝██║██╔██║ █████╔╝███████╗                        
██║     ██║   ██║██║╚██╗██║██║╚██╗██║██╔══╝  ██║        ██║       ██╔══╝  ██║   ██║██║   ██║██╔══██╗    ██╔═══╝ ████╔╝██║██╔═══╝ ██╔═══██╗                       
╚██████╗╚██████╔╝██║ ╚████║██║ ╚████║███████╗╚██████╗   ██║       ██║     ╚██████╔╝╚██████╔╝██║  ██║    ███████╗╚██████╔╝███████╗╚██████╔╝                       
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝ ╚═════╝   ╚═╝       ╚═╝      ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝                        
                                                                                                                                                                 

''',)
time.sleep(1)
while True:
    player[1]['name'] = input("What is player 1's 3 letter name?").upper()
    if len(player[1]['name']) != 3 or not (player[1]['name'].isalpha()):
        print('3 alphabet letters please.')
    else:
        break
while True:
    player[2]['name'] = input("What is player 2's 3 letter name?").upper()
    if len(player[2]['name']) != 3 or not (player[2]['name'].isalpha()):
        print('3 alphabet letters please.')
    elif player[2]['name'] == player[1]['name']:
        print('Names cannot be the same.')
    else:
        break
# generate game board
def generateBoard():
    global board, rows, columns
    rows = 6
    columns = 7
    board = np.full((rows, columns), '◯')
    return board
generateBoard()
def checkWin():
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
    for column in range(columns - 3):
        for row in range(rows - 3):
            if board[row][column] in ('●', '■'):
                if board[row][column] == board[row + 1][column+1] == board[row + 2][column+2] == board[row + 3][column+3]:
                    winDirection = 'diagonally'
                    return True
# check diagonal negative
    for column in range(3, columns):
        for row in range(rows - 3):
            if board[row][column] in ('●', '■'):
                if board[row][column] == board[row + 1][column-1] == board[row + 2][column-2] == board[row + 3][column-3]:
                    winDirection = 'diagonally'
                    return True
def checkDraw():
    return '◯' not in board

def playGame():
    global gameResults
    global player
    gaming = True
    while gaming:
        for i in player:
            print(board)
            if checkDraw():
                print('Draw! Nobody wins!')
                gaming = False
                gameResults = f'''/// GAME {datetime.datetime.now().strftime("%I:%M:%S %p on %B %d, %Y")} ///
                                    Players:
                                        1 - {player[1]['name']}
                                        2 - {player[2]['name']}
                    Game drew!! Nobody wins.'''
                break
            else:
                print(f"{player[i]['name']}'s turn")
            while True:
                column = int(input(f'Select column 1 to {columns}')) - 1
                full = True
                # check column from bottom to top, drop if empty
                for row in range(rows - 1, -1, -1):
                    if board[row][column] == '◯':
                        board[row][column] = player[i]['piece']
                        full = False
                        break
                if full:
                    print('Column Full')
                else:
                    break
            if checkWin():
                winningPlayer = player[i]
                player[i]['finalScore'] = player[i]['score']
                print(f'{player[i]['name']} wins {winDirection} with {player[i]['finalScore']} points left!')
                print(board)
                gaming = False
                gameResults = f'''/// GAME {datetime.datetime.now().strftime("%I:%M:%S %p on %B %d, %Y")} ///
                Players:
                    1 - {player[1]['name']}
                    2 - {player[2]['name']}
                Winning Player: 
                {winningPlayer['name']} with {winningPlayer['finalScore']} points.
                Final board state:
                {board} 

                '''
                break
            # if they havent placed the winning piece, subtract points.
            # not sure if i should subtract points when they place the winning piece
            # i think not
            player[i]['score'] -= 2

playGame()
print('Game Over')


# save results to file
save = input(f'Would you like to save your results? Y/N ')
if save.lower() == 'y':
    print('Looking for previous results...')
    try:
        f = open("CFResults.txt")
        print('File found!')
        with open("CFResults.txt", "a") as f:
            f.write(gameResults)
            f.close()



    except:
        print('Results file not found. Creating...')
        f = open("CFResults.txt", "x")
        with open("CFResults.txt", "a") as f:
            f.write(gameResults)
        f.close()
    print(f"File saved to {pathlib.Path().resolve()}")
