def playgame():
    player = 1
    while True:
        column = int(input(f'Select column 1 to {columns}')) - 1
        # check column from bottom to top, drop if empty
        full = True
        for row in range(rows - 1, -1, -1):
            if board[row][column] == '◯' and player == 1:
                board[row][column] = '●'
                player = 2
                print(board)
                print('now' + f'{player}')
            elif board[row][column] == '◯' and player == 2:
                board[row][column] = '■'
                player = 1
                print(board)
                print('now' + f'{player}')

            full = False
            break
        if full == True:
            print('Board Full')
playgame()