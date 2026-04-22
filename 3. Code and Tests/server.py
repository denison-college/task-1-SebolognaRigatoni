import time
import struct
import socket
import threading
import numpy as np
import datetime
import os

# networking possible thanks to this guy https://www.youtube.com/watch?v=VvwLXnY-mKk

class Server:
    def __init__(self, host='localhost', port=62743):
        self.host = host
        self.port = port
        self.kill = False
        self.thread_count = 0

        self.board = np.full((self.rows, self.columns), '◯')
        self.columns = 0
        self.rows = 0
        self.player = {
            1: {'player': '0', 'name': '', 'score': 100, 'piece': '●', 'finalScore': 0},
            2: {'player': '1', 'name': '', 'score': 100, 'piece': '■', 'finalScore': 0}
        }

        self.players = []

    def clearConsole(self):
        os.system('cls' if os.name == 'nt' else 'clear')

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
    def serialize(self):
        return struct.pack('BB9s', self.turn, ord(self.winner), ''.join(self.board).encode('utf-8'))
    def place(self, conn, space_index):
        gaming = True
        while gaming:
            for i in self.player:
                print(self.board)
                print(''' 1    2   3   4   5   6   7''')
                if self.checkDraw():
                    print('Draw! Nobody wins!')
                    self.gameResults = (
                        f"/// GAME {datetime.datetime.now().strftime('%I:%M:%S %p on %B %d, %Y')} ///\n"
                        f"Players:\n"
                        f"\t1 - {self.player[1]['name']}\n"
                        f"\t2 - {self.player[2]['name']}\n"
                        f"Game drew!! Nobody wins.\n\n"
                        f"Final board state:\n"
                        f"{self.board} \n\n"
                    )
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
                    self.player[i]['finalScore'] = self.player[i]['score']
                    print(
                        f'{self.player[i]['name']} wins {self.winDirection} with {self.player[i]['finalScore']} points left!')
                    print(self.board)
                    gaming = False
                    self.winner = self.player[i]
                    self.gameResults = (
                        f"/// GAME {datetime.datetime.now().strftime('%I:%M:%S %p on %B %d, %Y')} /// \n"
                        f"Players:\n"
                        f"  1 - {self.player[1]['name']}\n"
                        f"  2 - {self.player[2]['name']}\n"
                        f"Winning Player: \n"
                        f"  {self.winner['name']} with {self.winner['finalScore']} points.\n"
                        f"Final board state:\n"
                        f"{self.board} \n\n"
                    )
                    break
                # if they havent placed the winning piece, subtract points.
                # not sure if i should subtract points when they place the winning piece
                # i think not
                self.player[i]['score'] -= 2
                self.clearConsole()
    def run_listener(self, conn):
        self.thread_count += 1
        conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)
        conn.settimeout(1)
        with conn:
            while not self.kill:
                try:
                    data = conn.recv(4096)
                    if len(data):
                        target_space = struct.unpack_from('B', data, 0)[0]
                        self.place(conn, target_space)
                except socket.timeout:
                    pass
        self.thread_count -= 1
        pass
    def connect_listen_loop(self):
        self.thread_count += 1
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
            s.bind((self.host, self.port))
            while not self.kill:
                s.settimeout(1)
                s.listen()
                try:
                    conn, addr = s.accept()
                    print('new connection:', conn, addr)
                    if len(self.players) < 2:
                        self.players.append(conn)
                        threading.Thread(target=self.run_listener, args=(conn,)).start()
                except socket.timeout:
                    continue
                time.sleep(0.01)
        self.thread_count -= 1

    def await_kill(self):
        self.kill = True
        while self.thread_count:
            time.sleep(0.01)
        print('killed')
    def run(self):
        threading.Thread(target=self.connect_listen_loop).start()
        try:
            while True:
                self.winner = self.checkWin()
                try:
                    for player_conn in self.players:
                        player_conn.send(self.serialize())
                except OSError:
                    pass
                time.sleep(0.05)
        except KeyboardInterrupt:
            self.await_kill()
Server().run()

