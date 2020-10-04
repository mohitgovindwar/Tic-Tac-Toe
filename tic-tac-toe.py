import random

def display(board):
    print(f'''
    {board[7]}|{board[8]}|{board[9]}                       7 | 8 | 9
    ---+---+---                      ---+---+---
    {board[4]}|{board[5]}|{board[6]}        Positions->    4 | 5 | 6
    ---+---+---                      ---+---+---
    {board[1]}|{board[2]}|{board[3]}                       1 | 2 | 3
    ''')

def valid_input():
    while True:
        pos = input("Enter position: ")
        if pos != ' ':
            if int(pos) in range(1, 10):
                pos = int(pos)
                break
            print('Not valid position\n')
        else:
            print("Thank you for playing Tic-Tac-Toe!")
            exit()
    return int(pos)

def valid_pos(turn, board):
    print(f'{turn} chance')
    pos = valid_input()
    while True:
        if board[pos] == '   ':
            board[pos] = turn
            break
        else:
            print('Cannot Overwrite, Plz select new loc')
            pos = valid_input()

def check(board):
    flag = 0
    if board[1] == board[2] == board[3] != '   ' or board[4] == board[5] == board[6] != '   ' or board[7] == board[8] == board[9] != '   ':
        flag = 1
    elif board[1] == board[4] == board[7] != '   ' or board[2] == board[5] == board[8] != '   ' or board[3] == board[6] ==board[9] != '   ':
        flag = 1
    elif board[1] == board[5] == board[9] != '   ' or board[3] == board[5] == board[7] != '   ':
        flag = 1
    return flag

def userInput(board, symbol):
    sym1, sym2 = symbol[random.randint(0, 1)]
    print(f'{sym1} is going first\n\n')
    display(board)
    for i in range(9):
        if i % 2 == 0:
            turn = ' ' + sym1 + ' '
            valid_pos(turn, board)
        else:
            turn = ' ' + sym2 + ' '
            valid_pos(turn, board)
        display(board)
        if i >= 4:
            if check(board):
                display(board)
                print(f'{turn} WON')
                break
        if i == 8:
            print("None WON, It's a TIE")

def game():
    board = ["Just to adjust location :)", '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ']
    symbol = [('X', 'O'), ('O', 'X')]
    while True:
        marker = input('\nEnter your Marker: ').upper()
        if marker == 'X' or marker == 'O':
            userInput(board, symbol)
            break
        else:
            print('Wrong Marker(X, O) please enter again.\n')

def main():
    again = 'Y'
    while again == 'Y':
        print('Press [space] for input whenever you want to stop the game')
        game()
        again = input('Press "Y/y" To Play Again?: ').upper()

main()