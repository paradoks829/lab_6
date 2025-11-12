def print_board(board):
    """Выводит доску в красивом виде, как в настоящей игре."""
    print("\n+----+----+----+----+")
    for i in board:
        line = "|"
        for j in i:
            line += f"{j:>3} |"
        print(line)
        print("+----+----+----+----+")

def game_logic(game_board):
    if game_board == win_board:    #Проверка на победный сценарий
        print('Победа')
        return
    else:    #Ищем пустую клетку для передачи её в movement
        print_board(game_board)
        for x in range(len(game_board)):
            for y in range(len(game_board[x])):
                if game_board[x][y] == empty_cell:
                    x_empty = x    #Столбец
                    y_empty = y    #Строка
                    break
    move = input('Куда двигаемся? W A S D: \n').lower()
    if move == 'w' or move == 'a' or move == 's' or move == 'd':
        movement(move, x_empty, y_empty)
    else:
        print('Нет такого направления')
        game_logic(game_board)

def movement(move, x_empty, y_empty):
    match move:
        case 'w':
            if x_empty - 1 >= 0:
                game_board[x_empty - 1][y_empty], game_board[x_empty][y_empty] = game_board[x_empty][y_empty], game_board[x_empty - 1][y_empty]
                game_logic(game_board)
            else:
                print('Туда низя')
                game_logic(game_board)
        case 'a':
            if y_empty - 1 >= 0:
                game_board[x_empty][y_empty - 1], game_board[x_empty][y_empty] = game_board[x_empty][y_empty], game_board[x_empty][y_empty - 1]
                game_logic(game_board)
            else:
                print('Туда низя')
                game_logic(game_board)
        case 's':
            if x_empty + 1 <= 3:
                game_board[x_empty + 1][y_empty], game_board[x_empty][y_empty] = game_board[x_empty][y_empty], game_board[x_empty + 1][y_empty]
                game_logic(game_board)
            else:
                print('Туда низя')
                game_logic(game_board)
        case 'd':
            if y_empty + 1 <= 3:
                game_board[x_empty][y_empty + 1], game_board[x_empty][y_empty] = game_board[x_empty][y_empty], game_board[x_empty][y_empty + 1]
                game_logic(game_board)
            else:
                print('Туда низя')
                game_logic(game_board)

empty_cell = ' x '
game_board = [[' 1 ', ' 2 ', ' 3 ', ' 4 '], [' 5 ', ' 6 ', ' 7 ', ' 8 '], [' 9 ', '10 ', '11 ', '12 '], ['13 ', '14 ', empty_cell, '15 ']]
win_board  = [[' 1 ', ' 2 ', ' 3 ', ' 4 '], [' 5 ', ' 6 ', ' 7 ', ' 8 '], [' 9 ', '10 ', '11 ', '12 '], ['13 ', '14 ', '15 ', empty_cell]]
game_logic(game_board)

