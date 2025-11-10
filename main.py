empty_cell = ' x '

game_board = [[' 1 ', ' 3 ', ' 4 ', ' 4 '], [' 5 ', ' 7 ', ' 6 ', ' 8 '], [' 9 ', '10 ', empty_cell, '11 '], ['13 ', '14 ', '15 ', '12 ']]
win_board  = [[' 1 ', ' 2 ', ' 3 ', ' 4 '], [' 5 ', ' 6 ', ' 7 ', ' 8 '], [' 9 ', '10 ', '11 ', '12 '], ['13 ', '14 ', '15 ', empty_cell]]

def game_logic(game_board):
    print('\n', game_board[0], '\n', game_board[1], '\n', game_board[2], '\n', game_board[3], '\n')
    if game_board == win_board:    #Проверка на победный сценарий
        return 'You won!'
    else:    #Ищем пустую клетку для передачи её в movement
        for x in range(len(game_board)):
            for y in range(len(game_board[x])):
                if game_board[x][y] == empty_cell:
                    x_empty = x    #Столбец
                    y_empty = y    #Строка
                    break
        print(x_empty,y_empty)
    move = input('Куда двигаемся? W A S D: \n').lower()
    movement(move, x_empty, y_empty)

def movement(move, x_empty, y_empty):
    match move:
        case 'w':
            game_board[x_empty - 1][y_empty], game_board[x_empty][y_empty] = game_board[x_empty][y_empty], game_board[x_empty - 1][y_empty]
            print(game_board[0])
            print(game_board[1])
            print(game_board[2])
            print(game_board[3])
        case 'a':
            game_board[x_empty][y_empty - 1], game_board[x_empty][y_empty] = game_board[x_empty][y_empty], game_board[x_empty][y_empty - 1]
            print(game_board[0])
            print(game_board[1])
            print(game_board[2])
            print(game_board[3])
        case 's':
            game_board[x_empty + 1][y_empty], game_board[x_empty][y_empty] = game_board[x_empty][y_empty], game_board[x_empty + 1][y_empty]
            print(game_board[0])
            print(game_board[1])
            print(game_board[2])
            print(game_board[3])
        case 'd':
            game_board[x_empty][y_empty + 1], game_board[x_empty][y_empty] = game_board[x_empty][y_empty], game_board[x_empty][y_empty + 1]
    print(game_board[0])
    print(game_board[1])
    print(game_board[2])
    print(game_board[3])

print(game_logic(game_board))
