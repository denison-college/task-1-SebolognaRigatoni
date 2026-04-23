import numpy as np
import datetime
import pathlib
import time
import sys
import pygame
import os
from colorist import Color, yellow, red
gameResults = ''
board = None
columns = 7
rows = 6
def slowprint(text, texttime):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(texttime)
def clearConsole():
    os.system('cls' if os.name=='nt' else 'clear')
# Pieces: '◯' for empty slot, '●' for p1, '■' for p2
# create players
player = {
    1: {'name': '', 'score': 100, 'piece': '●', 'finalScore': 0},
    2: {'name': '', 'score': 100, 'piece': '■', 'finalScore': 0}
    }
pygame.mixer.init()
def introSequence():
    try:
        intro = pygame.mixer.Sound('intro.wav')
    except:
        intro = pygame.mixer.Sound('3. Code and Tests\intro.wav')
    intro.play()
    clearConsole()
    time.sleep(0.8)
    slowprint('WELCOME TO\n', 0.0015)
    time.sleep(2.5)
    slowprint('THE BEST EXPERIENCE IN ALL OF PYTHON GAMING HISTORY\n', 0.0015)
    time.sleep(2.8)
    slowprint('AVAILABLE EXCLUSIVELY FOR BATHURST HIGH SOFTWARE ENGINEERING STUDENTS\n', 0.0015)
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
                                                                                                                                                                    

    ''', 0.0015)
    time.sleep(1)
def playerSetup():
    while True:
        player[1]['name'] = input("What is player 1's name? (12 letters max) ").upper()
        if len(player[1]['name']) > 12 or not (player[1]['name'].isalpha()):
            print('12 alphabet letters only.')
        else:
            break
    while True:
        player[2]['name'] = input("What is player 2's name? (12 letters max) ").upper()
        if len(player[2]['name']) > 12 or not (player[2]['name'].isalpha()):
            print('12 alphabet letters only.')
        elif player[2]['name'] == player[1]['name']:
            print('Names cannot be the same.')
        else:
            clearConsole()
            break
# generate game board
def generateBoard():
    global rows
    global columns
    global board
    board = np.full((rows, columns), '◯')
    return board
def boardSettings():
    global board, rows, columns
    while True:
        try:
            rows = int(input('How many rows 6-15? (recommended 6) '))
            if rows not in range(5, 16):
                print('As a digit between 6 and 15 please :)')
            else:
                break
        except ValueError:
            print('As a digit between 6 and 15 please :)')

    while True:
        try:
            columns = int(input('How many columns 6-15? (recommended 7) '))
            if columns not in range(5, 16):
                print('As a digit between 6 and 15 please :)')
            else:
                break
        except ValueError:
            print('As a digit between 6 and 15 please :)')
def saveResults():
    while True:
        save = input(f'Would you like to save your results? Y/N ')
        if save.lower() == 'y':
            print('Looking for previous results...')
            time.sleep(1)
            try:
                f = open("CFResults.txt")
                print('File found!')
                print('Saving...')
                time.sleep(2)
                with open("CFResults.txt", "a", encoding="utf-8") as f:
                    f.write(gameResults)
                    f.close()
            except FileNotFoundError:
                print('Results file not found. Creating...')
                time.sleep(2)
                f = open("CFResults.txt", "x")
                with open("CFResults.txt", "a", encoding="utf-8") as f:
                    f.write(gameResults)
                f.close()
            print(f"File saved to {pathlib.Path().resolve()} as CFResults.txt")
            try:
                again = input('Play again? Y/N')
                if again.lower() == 'y':
                    pygame.mixer.music.fadeout(5)
                    gameLoop()
                elif again == 'n':
                    sys.exit()
                else:
                    print('Y or N please')
            except ValueError:
                print('Y or N please')
            break
        elif save.lower() == 'n':
            try:
                again = input('Play again? Y/N')
                if again.lower() == 'y':
                    gameLoop()
                elif again == 'n':
                    sys.exit()
                else:
                    print('Y or N please')
            except ValueError:
                print('Y or N please')
        else:
            print('Invalid input. Please select Y or N.')

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
                gameResults = (
                        f"/// GAME {datetime.datetime.now().strftime('%I:%M:%S %p on %B %d, %Y')} ///\n"
                        f"Players:\n"
                        f"\t1 - {player[1]['name']}\n"
                        f"\t2 - {player[2]['name']}\n"
                        f"Game drew!! Nobody wins.\n\n"
                        f"Final board state:\n"
                        f"{board} \n\n"
                    )
                break
            else:
                print(f"{player[i]['name']}'s turn")
            while True:
                while True:
                    try:
                        question = input(f'Select column 1 to {columns}, or type q to quit: ')

                        if question == 'q':
                            print(f'{player[i]['name']} quits!')
                            gameResults = (
                                f"/// GAME {datetime.datetime.now().strftime('%I:%M:%S %p on %B %d, %Y')} ///\n"
                                f"Players:\n"
                                f"\t1 - {player[1]['name']}\n"
                                f"\t2 - {player[2]['name']}\n"
                                f"Game drew!! Nobody wins.\n\n"
                                f"Final board state:\n"
                                f"{board} \n\n"
                            )

                            gaming = False
                            saveResults()
                            break
                        else:
                            column = int(question) - 1
                        if column in range(columns):
                            break
                        else:
                            print('Out of range')
                    except ValueError:
                            print('Please type your number as a digit between 1 and 7.')
                full = True
                # check column from bottom to top, drop if empty
                for row in range(rows - 1, -1, -1):
                    if board[row][column] == '◯':
                        board[row][column] = player[i]['piece']
                        place = pygame.mixer.Sound('8 Bit-Hit - Free Sound Effect [HD].wav')
                        place.play()
                        full = False
                        break
                if full:
                    print('Column Full')
                else:
                    break
            if checkWin():
                pygame.mixer.music.load('Holy Lights.mp3')
                pygame.mixer.music.play()
                fireworks = pygame.mixer.Sound('Firework - Sound Effect (HD).mp3')
                fireworks.play()
                time.sleep(5)
                clearConsole()
                winningPlayer = player[i]
                player[i]['finalScore'] = player[i]['score']
                slowprint(f'{player[i]['name']} wins {winDirection} with {player[i]['finalScore']} points left!', 0.05)
                print(board)
                slowprint(f""" 
                        CELEBRATING {player[i]['name']}                             
                                        .
              . .                     -:-             .  .  .
            .'.:,'.        .  .  .     ' .           . \ | / .
            .'.;.`.       ._. ! ._.       \          .__\:/__.
             `,:.'         ._\!/_.                     .';`.      . ' .
             ,'             . ! .        ,.,      ..======..       .:.
            ,                 .         ._!_.     ||::: : | .        ',
     .====.,                  .           ;  .~.===: : : :|   ..===.
     |.::'||      .=====.,    ..=======.~,   |"|: :|::::::|   ||:::|=====|
  ___| :::|!__.,  |:::::|!_,   |: :: ::|"|l_l|"|:: |:;;:::|___!| ::|: : :|
 |: :|::: |:: |!__|; :: |: |===::: :: :|"||_||"| : |: :: :|: : |:: |:::::|
 |:::| _::|: :|:::|:===:|::|:::|:===F=:|"!/|\!"|::F|:====:|::_:|: :|::__:|
 !_[]![_]_!_[]![]_!_[__]![]![_]![_][I_]!//_:_\\![]I![_][_]!_[_]![]_!_[__]!
 -----------------------------------"---''''```---"-----------------------
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ |= _ _:_ _ =| _ _ _ _ _ _ _ _ _ _ _ _
                                     |=    :    =|                
_____________________________________L___________J________________________
--------------------------------------------------------------------------
MUSIC: LIL COITS - HOLY LIGHTS
""", 0.005)
                gaming = False
                gameResults = (
                    f"/// GAME {datetime.datetime.now().strftime('%I:%M:%S %p on %B %d, %Y')} \\\\n"
                    f"Players:\n"
                    f"  1 - {player[1]['name']}\n"
                    f"  2 - {player[2]['name']}\n"
                    f"Winning Player: \n"
                    f"  {winningPlayer['name']} with {winningPlayer['finalScore']} points.\n"
                    f"Final board state:\n"
                    f"{board} \n\n"
                )
                saveResults()
                break
            # if they havent placed the winning piece, subtract points.
            # not sure if i should subtract points when they place the winning piece
            # i think not
            player[i]['score'] -= 2
            clearConsole()

def menu():
    while True:
        ans = int(input('1. Local Play\n'
                        '2. View Log File\n'
                        '3. Board Settings\n'
                        '4. Quit Game\n'))

        try:
            if ans == 3:
                boardSettings()
            elif ans == 2:
                try:
                    with open("CFResults.txt", "r") as file:
                        print(file.read())
                        any = input('press any key ')
                except FileNotFoundError:
                    print('No file exists.')
            elif ans == 1:
                break
            elif ans == 4:
                quit
            else:
                print('Digit between 1 and 3.')
        except ValueError:
            print('Digit between 1 and 3')
def gameLoop():
    menu()
    playerSetup()
    generateBoard()
    playGame()
if __name__ == "__main__":
    introSequence()
    gameLoop()

# save results to file
