import random

board = [['1','2','3'],['4','5','6'],['7','8','9']]
occupied = []

def boarddraw():
    print("\n\t "+board[0][0]+" | "+board[0][1]+" | "+board[0][2])
    print("\t---+---+---")
    print("\t "+board[1][0]+" | "+board[1][1]+" | "+board[1][2])
    print("\t---+---+---")
    print("\t "+board[2][0]+" | "+board[2][1]+" | "+board[2][2]+"\n")

def xwin():
    win1 = 0
    if board[0] == ['X','X','X']:
        win1 = 1
    elif board[1] == ['X','X','X']:
        win1 = 1
    elif board[2] == ['X','X','X']:
        win1 = 1
    elif board[0][0] + board[1][0] + board[2][0] == 'XXX':
        win1 = 1
    elif board[0][1] + board[1][1] + board[2][1] == 'XXX':
        win1 = 1
    elif board[0][2] + board[1][2] + board[2][2] == 'XXX':
        win1 = 1
    elif board[0][0] + board[1][1] + board[2][2] == 'XXX':
        win1 = 1
    elif board[0][2] + board[1][1] + board[2][0] == 'XXX':
        win1 = 1
    return win1

def owin():
    win2 = 0
    if board[0] == ['O','O','O']:
        win2 = 1
    elif board[1] == ['O','O','O']:
        win2 = 1
    elif board[2] == ['O','O','O']:
        win2 = 1
    elif board[0][0] + board[1][0] + board[2][0] == 'OOO':
        win2 = 1
    elif board[0][1] + board[1][1] + board[2][1] == 'OOO':
        win2 = 1
    elif board[0][2] + board[1][2] + board[2][2] == 'OOO':
        win2 = 1
    elif board[0][0] + board[1][1] + board[2][2] == 'OOO':
        win2 = 1
    elif board[0][2] + board[1][1] + board[2][0] == 'OOO':
        win2 = 1
    return win2
    
def starter(begin = ["name1","name2"]):
    start = random.choice(begin)
    return start

def play1(player1):
    print(player1+", please enter where you want to place an X")
    retry = 0
    x = int(input("Enter number: "))
    while x in occupied:
        print("Already occupied...")
        x = int(input("Enter number: "))
    occupied.append(x)
    if x == 1:
        board[0][0] = 'X'
    elif x == 2:
        board[0][1] = 'X'
    elif x == 3:
        board[0][2] = 'X'
    elif x == 4:
        board[1][0] = 'X'
    elif x == 5:
        board[1][1] = 'X'
    elif x == 6:
        board[1][2] = 'X'
    elif x == 7:
        board[2][0] = 'X'    
    elif x == 8:
        board[2][1] = 'X'
    elif x == 9:
        board[2][2] = 'X'
    else:
        print("Please enter a number from 1 to 9")
        retry = 1
    return retry

def oneplayer():
    name1 = input("Please enter your name: ")
    name2 = 'Computer'
    print("Hello "+name1+"! You are playing a game against the "+name2)
    input("Press Enter to see who begins!")
    start = starter()
    if start == 'name1':
        print(name1+" goes first!")
    else:
        print("Sorry, the "+name2+" goes first")
    boarddraw()

def play2(player2):
    print(player2+", please enter where you want to place an O")
    retry = 0
    x = int(input("Enter number: "))
    while x in occupied:
        print("Already occupied...")
        x = int(input("Enter number: "))
    occupied.append(x)
    if x == 1:
        board[0][0] = 'O'
    elif x == 2:
        board[0][1] = 'O'
    elif x == 3:
        board[0][2] = 'O'
    elif x == 4:
        board[1][0] = 'O'
    elif x == 5:
        board[1][1] = 'O'
    elif x == 6:
        board[1][2] = 'O'
    elif x == 7:
        board[2][0] = 'O'    
    elif x == 8:
        board[2][1] = 'O'
    elif x == 9:
        board[2][2] = 'O'
    else:
        print("Please enter a number from 1 to 9")
        retry = 1
    return retry

def twoplayer():
    name1 = input("Player 1, please enter your name: ")
    name2 = input("Player 2, please enter your name: ")
    print("\nHello "+name1+" and "+name2+"!\n")
    input("Press Enter to see who begins!\n")
    start = starter()
    if start == 'name1':
        print(name1+" goes first!")
        player1 = name1
        player2 = name2
    else:
        print(name2+" goes first!")
        player1 = name2
        player2 = name1
    win1 = 0
    win2 = 0
    while win1 == 0 or win2 == 0:
        print(player1+", it's your turn now!")
        boarddraw()
        retry = play1(player1)
        if retry == 1:
            boarddraw()
            print("foutje")
            retry = play1(player1)
        win1 = xwin()
        if win1 == 1:
            break
        elif len(occupied) == 9:
            break
        print(player2+", it's your turn now!")
        boarddraw()
        retry = play2(player2)
        if retry == 1:
            boarddraw()
            retry = play2(player2)
        win2 = owin()
        if win2 == 1:
            break
        elif len(occupied) == 9:
            break
    return win1, win2, player1, player2

print("\nWelcome to Tic Tac Toe! Coded by Jeroen Penders\n")

win1, win2, player1, player2 = twoplayer()
boarddraw()
if win1 == 1:
    print("\n"+player1+" has won the game!!\n")
elif win2 == 1:
    print("\n"+player2+" has won the game!!\n")
else:
    print("\nThe game is a draw...\n")






    

