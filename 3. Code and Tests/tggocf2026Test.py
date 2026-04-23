import numpy as np
import pytest
import tggocf2026 as game


def BoardSetup():
    game.rows = 12
    game.columns = 9
    game.board = np.full((game.rows, game.columns), '◯')


def testBoardShape():
    board = game.generateBoard()
    assert board.shape == (game.rows, game.columns)


def testEmptyBoard():
    board = game.generateBoard()
    assert np.all(board == '◯')


# draw test
def testDraw():
    game.board = np.full((6, 7), '●')
    assert game.checkDraw() is True


def testDrawFalse():
    game.board[0][0] = '◯'
    assert game.checkDraw() is False


# win test code
def testRow():
    game.board[0][0:4] = ['●', '●', '●', '●']
    assert game.checkWin() is True



def testColumn():
    for i in range(4):
        game.board[i][0] = '■'
    assert game.checkWin() is True



def testDiagonalPositive():
    for i in range(4):
        game.board[i][i] = '●'
    assert game.checkWin() is True



def testDiagonalNegative():
    for i in range(4):
        game.board[i][3 - i] = '■'
    assert game.checkWin() is True



# test no win
def checkWinFalse():
    assert game.checkWin() is false