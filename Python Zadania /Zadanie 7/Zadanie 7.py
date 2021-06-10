board = {1: ' ',2: ' ',3: ' ',
         4: ' ',5: ' ',6: ' ',
         7: ' ',8: ' ',9: ' ' }

def print_board(board):
    print(board[1]+ '|'+board[2]+ '|'+board[3])
    print('-+-+-')
    print(board[4]+ '|'+board[5]+ '|'+board[6])
    print('-+-+-')
    print(board[7]+ '|'+board[8]+ '|'+board[9])
    print('-+-+-')

print_board(board)

def spaceIsFree(postion):
    if(board[postion]==' '):
        return True
    else:
        return False

def insertLetter(letter,position):
    if spaceIsFree(position):
        board[position] = letter
        print_board(board)
        print('\n')
        if checkdraw():
            print("Remis!")
            exit()
        if check_win():
            if letter =="X":
                print("Bot wygral!")
                exit()
            else:
                print("Gracz wygral!")
                exit()
    else:
        print("Zajete miejsce")
        position = int(input("Wpisz nowa pozycje"))
        insertLetter(letter,position)
        return

def checkdraw():
    for key in board.keys():
        if board[key] ==' ':
            return False
    return True

def check_win():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

def check_mark_won(mark):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False

player = 'O'
bot = 'X'
def playerMove():
    position = int(input("Wpisz pozycje dla kolka: "))
    insertLetter(player,position)
    return

def compMove():
    #position = int(input("Wpisz pozycje dla krzyzyka: "))
    #insertLetter(bot,position)
    best_score = -1000
    best_move = 0

    for key in board.keys():
        if board[key]==' ':
            board[key] = bot
            score = minimax(board,0,False)
            board[key] = ' '
            if score >best_score:
                best_score = score
                best_move = key
    insertLetter(bot,best_move)
    return

def minimax(board, depth, isMaximizing):
    if (check_mark_won(bot)):
        return 1
    elif (check_mark_won(player)):
        return -1
    elif (checkdraw()):
        return 0

    if (isMaximizing):
        bestScore = -800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore

while not check_win():
    compMove()
    playerMove()
    #compMove()