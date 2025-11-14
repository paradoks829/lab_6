import random
import os 
import time

def clear_s():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    """Выводит доску в красивом виде, как в настоящей игре."""
    print("\n+----+----+----+----+")
    for i in board:
        line = "|"
        for j in i:
            line += f"{j:>3} |"
        print(line)
        print("+----+----+----+----+")

def text(m):
    clear_s()
    print_board(game_board)
    print(f"\n{m}")
    time.sleep(1)

def game_logic(game_board):
    if game_board == win_board:    #Проверка на победный сценарий
        clear_s()
        print('Победа')
        return
    else:    #Ищем пустую клетку для передачи её в movement
        clear_s()
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
        text('Нет такого направления')
        game_logic(game_board)

def movement(move, x_empty, y_empty):
    match move:
        case 'w':
            if x_empty - 1 >= 0:
                game_board[x_empty - 1][y_empty], game_board[x_empty][y_empty] = game_board[x_empty][y_empty], game_board[x_empty - 1][y_empty]
                game_logic(game_board)
            else:
                text("Туда нельзя!")
                game_logic(game_board)
        case 'a':
            if y_empty - 1 >= 0:
                game_board[x_empty][y_empty - 1], game_board[x_empty][y_empty] = game_board[x_empty][y_empty], game_board[x_empty][y_empty - 1]
                game_logic(game_board)
            else:
                text("Туда нельзя!")
                game_logic(game_board)
        case 's':
            if x_empty + 1 <= 3:
                game_board[x_empty + 1][y_empty], game_board[x_empty][y_empty] = game_board[x_empty][y_empty], game_board[x_empty + 1][y_empty]
                game_logic(game_board)
            else:
                text("Туда нельзя!")
                game_logic(game_board)
        case 'd':
            if y_empty + 1 <= 3:
                game_board[x_empty][y_empty + 1], game_board[x_empty][y_empty] = game_board[x_empty][y_empty], game_board[x_empty][y_empty + 1]
                game_logic(game_board)
            else:
                text("Туда нельзя!")
                game_logic(game_board)

empty_cell = '   '
win_board  = [[' 1 ', ' 2 ', ' 3 ', ' 4 '], [' 5 ', ' 6 ', ' 7 ', ' 8 '], [' 9 ', '10 ', '11 ', '12 '], ['13 ', '14 ', '15 ', empty_cell]]

game_board = [x[:] for x in win_board]
x, y = 3, 3
for _ in range(50):
    d = []
    if x > 0: d.append('w')
    if x < 3: d.append('s')
    if y > 0: d.append('a')
    if y < 3: d.append('d')
    move = random.choice(d)
    if move == 'w':
        game_board[x][y], game_board[x-1][y] = game_board[x-1][y], game_board[x][y]
        x -= 1
    elif move == 's':
        game_board[x][y], game_board[x+1][y] = game_board[x+1][y], game_board[x][y]
        x += 1
    elif move == 'a':
        game_board[x][y], game_board[x][y-1] = game_board[x][y-1], game_board[x][y]
        y -= 1
    elif move == 'd':
        game_board[x][y], game_board[x][y+1] = game_board[x][y+1], game_board[x][y]
        y += 1

clear_s()
print('игра началась')
time.sleep(1)
clear_s()
game_logic(game_board)
