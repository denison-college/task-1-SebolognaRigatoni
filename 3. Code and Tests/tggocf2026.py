import sys
import struct
import threading
import socket
import numpy as np
import datetime
import pathlib
import time
import sys
import pygame
import os
from colorist import Color, yellow, red



# Pieces: '◯' for empty slot, '●' for p1, '■' for p2
# create players
class tggocf:
    def __init__(self):
        self.gameResults = ''
        self.board = None
        self.columns = 0
        self.rows = 0
        self.player = {
            1: {'name': '', 'score': 100, 'piece': '●', 'finalScore': 0},
            2: {'name': '', 'score': 100, 'piece': '■', 'finalScore': 0}
        }

    def slowprint(self, text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.0015)

    def clearConsole(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def introSequence(self):
        try:
            intro = pygame.mixer.Sound('intro.wav')
        except:
            intro = pygame.mixer.Sound('3. Code and Tests\intro.wav')
        intro.play()
        self.clearConsole()
        time.sleep(0.8)
        self.slowprint('WELCOME TO\n')
        time.sleep(2.5)
        self.slowprint('THE BEST EXPERIENCE IN ALL OF PYTHON GAMING HISTORY\n')
        time.sleep(2.8)
        self.slowprint('AVAILABLE EXCLUSIVELY FOR BATHURST HIGH SOFTWARE ENGINEERING STUDENTS\n')
        time.sleep(2.5)
        self.slowprint('''


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


        ''', )
        time.sleep(1)

    def generateBoard(self):
        self.rows = 6
        self.columns = 7
        self.board = np.full((self.rows, self.columns), '◯')
        return self.board

    def generatePlayers(self):
        while True:
            self.player[1]['name'] = input("What is player 1's 3 letter name?").upper()
            if len(self.player[1]['name']) != 3 or not (self.player[1]['name'].isalpha()):
                print('3 alphabet letters please.')
            else:
                break
        while True:
            self.player[2]['name'] = input("What is player 2's 3 letter name?").upper()
            if len(self.player[2]['name']) != 3 or not (self.player[2]['name'].isalpha()):
                print('3 alphabet letters please.')
            elif self.player[2]['name'] == self.player[1]['name']:
                print('Names cannot be the same.')
            else:
                break
        self.clearConsole()
    def checkWin(self):
        # check horizontal
        for row in range(self.rows):
            for column in range(self.columns - 3):
                if self.board[row][column] in ('●', '■'):
                    if self.board[row][column] == self.board[row][column + 1] == self.board[row][column + 2] == self.board[row][column + 3]:
                        self.winDirection = 'horizontally'
                        return True
        # check vertical
        for column in range(self.columns):
            for row in range(self.rows - 3):
                if self.board[row][column] in ('●', '■'):
                    if self.board[row][column] == self.board[row + 1][column] == self.board[row + 2][column] == self.board[row + 3][column]:
                        self.winDirection = 'vertically'
                        return True
        # check diagonal positive
        for column in range(self.columns - 3):
            for row in range(self.rows - 3):
                if self.board[row][column] in ('●', '■'):
                    if self.board[row][column] == self.board[row + 1][column + 1] == self.board[row + 2][column + 2] == self.board[row + 3][
                        column + 3]:
                        self.winDirection = 'diagonally'
                        return True
        # check diagonal negative
        for column in range(3, self.columns):
            for row in range(self.rows - 3):
                if self.board[row][column] in ('●', '■'):
                    if self.board[row][column] == self.board[row + 1][column - 1] == self.board[row + 2][column - 2] == self.board[row + 3][
                        column - 3]:
                        self.winDirection = 'diagonally'
                        return True
    def checkDraw(self):
        return '◯' not in self.board
    def playGame(self):
        gaming = True
        while gaming:
            for i in self.player:
                print(self.board)
                print(''' 1    2   3   4   5   6   7''')
                if self.checkDraw():
                    print('Draw! Nobody wins!')
                    gaming = False
                    break
                else:
                    print(f"{self.player[i]['name']}'s turn")
                while True:
                    while True:
                        try:
                            column = int(input(f'Select column 1 to {self.columns}: ')) - 1
                            if column in range(self.columns):
                                break
                            else:
                                print('Out of range')
                        except ValueError:
                            print('Please type your number as a digit between 1 and 7.')
                    full = True
                    # check column from bottom to top, drop if empty
                    for row in range(self.rows - 1, -1, -1):
                        if self.board[row][column] == '◯':
                            self.board[row][column] = self.player[i]['piece']
                            full = False
                            break
                    if full:
                        print('Column Full')
                    else:
                        break
                if self.checkWin():
                    self.clearConsole()
                    winningPlayer = self.player[i]
                    self.player[i]['finalScore'] = self.player[i]['score']
                    print(f'{self.player[i]['name']} wins {self.winDirection} with {self.player[i]['finalScore']} points left!')
                    print(self.board)
                    gaming = False
                    self.gameResults = (
    f"/// GAME {datetime.datetime.now().strftime('%I:%M:%S %p on %B %d, %Y')} ///\n"
    f"Players:\n"
    f"\t1 - {self.player[1]['name']}\n"
    f"\t2 - {self.player[2]['name']}\n"
    f"Game drew!! Nobody wins.\n\n"
)
                    self.gameResults = (
                        f"/// GAME {datetime.datetime.now().strftime('%I:%M:%S %p on %B %d, %Y')} /// \n"
                        f"Players:\n"
                        f"  1 - {self.player[1]['name']}\n"
                        f"  2 - {self.player[2]['name']}\n"
                        f"Winning Player: \n"
                        f"  {winningPlayer['name']} with {winningPlayer['finalScore']} points.\n"
                        f"Final board state:\n"
                        f"{self.board} \n\n"
                    )
                    break
                # if they havent placed the winning piece, subtract points.
                # not sure if i should subtract points when they place the winning piece
                # i think not
                self.player[i]['score'] -= 2
                self.clearConsole()

    def saveFile(self):
        # save results to file
        while True:
            save = input(f'Would you like to save your results? Y/N ')
            if save.lower() == 'y':
                print('Looking for previous results...')
                try:
                    f = open("CFResults.txt")
                    print('File found!')
                    with open("CFResults.txt", "a", encoding="utf-8") as f:
                        f.write(self.gameResults)
                        f.close()
                except FileNotFoundError:
                    print('Results file not found. Creating...')
                    f = open("CFResults.txt", "x")
                    with open("CFResults.txt", "a", encoding="utf-8") as f:
                        f.write(self.gameResults)
                    f.close()
                print(f"File saved to {pathlib.Path().resolve()} as CFResults.txt")
                break
            elif save.lower() == 'n':
                print('Cya later space cowboy.')
                break
            else:
                print('Invalid input. Please select Y or N.')




pygame.mixer.init()




class gameClient:
    def __init__(self, host='127.0.0.1', port=62743):
        self.host = host
        self.port = port
        self.socket = None
        self.game = tggocf()
    def run_listener(self):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
            s.connect((self.host, self.port))
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)
            s.settimeout(1)
            print('connected', s)
            self.socket = s

    def run(self):
        print('Running listener..')
        threading.Thread(target=self.run_listener).start()
        time.sleep(1)
        self.game.introSequence()
        self.game.generateBoard()
        self.game.generatePlayers()
        self.game.playGame()
        self.game.saveFile()


client = gameClient()
client.run()


