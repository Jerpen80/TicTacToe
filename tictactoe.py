import random
import time

# ASCII Art
def art():
    print("""
 ______             ______                  ______                  
/\__  _\__         /\__  _\                /\__  _\                 
\/_/\ \/\_\    ___ \/_/\ \/    __      ___ \/_/\ \/   ___      __   
   \ \ \/\ \  / ___\  \ \ \  / __ \   / ___\  \ \ \  / __ \  / __ \ 
    \ \ \ \ \/\ \__/   \ \ \/\ \_\ \_/\ \__/   \ \ \/\ \_\ \/\  __/ 
     \ \_\ \_\ \____\   \ \_\ \__/ \_\ \____\   \ \_\ \____/\ \____\ 
      \/_/\/_/\/____/    \/_/\/__/\/_/\/____/    \/_/\/___/  \/____/""") 
    print("\t\t\t\t\t\t   By Jeroen Penders\n")

# Board in dictionary
board = {1: ' ',2: ' ',3: ' ',4: ' ',5: ' ',6: ' ',7: ' ',8: ' ',9: ' '}

# Determines who starts
def start(starter = ['p1','p2']):
    starter = random.choice(starter)
    return starter

# How to play
def manual():
    print("The numbers of the positions are as follows:")
    print("\n\t 1 | 2 | 3")
    print("\t---+---+---")
    print("\t 4 | 5 | 6")
    print("\t---+---+---")
    print("\t 7 | 8 | 9")

# Draw the board
def boarddraw(board):
    print("\n\t "+board[1]+" | "+board[2]+" | "+board[3])
    print("\t---+---+---")
    print("\t "+board[4]+" | "+board[5]+" | "+board[6])
    print("\t---+---+---")
    print("\t "+board[7]+" | "+board[8]+" | "+board[9]+"\n")

# AI lines just for fun
def fun():
    choices = ["Geez, I can't think straight...","E = mc², so my next move must be.....",
    "If my calculations are correct...","Information overload....","1 + 1 makes 2, so in that case...",
    "Uhm...", "Please don't look at me while I'm thinking.."]
    line = random.choice(choices)
    return line

# AI lines also for fun
def fun2():
    choices = ["Ha, what do you think of this move!","Well, let's hope for the best..","I'm winning with this killer move!",
    "Prepare to lose!","Gotcha!","I'm just gonna pick one.."]
    line = random.choice(choices)
    return line

# Check if position is empty
def empty(number):
    if board[number] == ' ':
        return True
    else:
        return False

# Placing mark on the board for player who is is X
def placemove1(player1, number):
    if empty(number):
        board[number] = player1
        boarddraw(board) 
        if winx():
            print(name2+" wins!!!\n")
            exit()
        
        if wino():
            print(name1+" wins!!!\n")
            exit()
            
        if draw():
            print("It's a draw...\n")
            exit()
        return
    else:
        print("Position already taken")
        number = int(input("Please select an empty position: "))
        placemove1(player1, number)
        return

# Placing mark on the board if DeepRetard is O
def placemove2(player2, number):
    if empty(number):
        board[number] = player2
        boarddraw(board) 
        if winx():
            print(name1+" wins!!!\n")
            exit()
        
        if wino():
            print(name2+" wins!!!\n")
            exit()
            
        if draw():
            print("It's a draw...\n")
            exit()
        return
    else:
        print("Position already taken")
        number = int(input("Please select an empty position: "))
        placemove2(player2, number)
        return

# Checks if player 1 wins the game
def winx():
    if board[1] + board[2] + board[3] == 'XXX':
        return True
    elif board[4] + board[5] + board[6] == 'XXX':
        return True
    elif board[7] + board[8] + board[9] == 'XXX':
        return True
    elif board[1] + board[4] + board[7] == 'XXX':
        return True
    elif board[2] + board[5] + board[8] == 'XXX':
        return True
    elif board[3] + board[6] + board[9] == 'XXX':
        return True
    elif board[1] + board[5] + board[9] == 'XXX':
        return True
    elif board[3] + board[5] + board[7] == 'XXX':
        return True
    else:
        return False

# Checks if player 2 wins the game
def wino():
    if board[1] + board[2] + board[3] == 'OOO':
        return True
    elif board[4] + board[5] + board[6] == 'OOO':
        return True
    elif board[7] + board[8] + board[9] == 'OOO':
        return True
    elif board[1] + board[4] + board[7] == 'OOO':
        return True
    elif board[2] + board[5] + board[8] == 'OOO':
        return True
    elif board[3] + board[6] + board[9] == 'OOO':
        return True
    elif board[1] + board[5] + board[9] == 'OOO':
        return True
    elif board[3] + board[5] + board[7] == 'OOO':
        return True
    else:
        return False

# Checks if the game is a draw
def draw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True

# asks for player 1 input
def player1move():
    number = 0
    while number not in range(1,10):
        number = int(input("Enter the number of the position where you want to play an 'X': "))
    placemove2(player1, number)
    return

# Asks for player 2 input
def player2move():
    number = 0
    while number not in range(1,10):
        number = int(input("Enter the number of the position where you want to play an 'O': "))
    placemove2(player2, number)
    return

# DeepRetard marks the board after minimax algorithm if AI is player 1
def compmove1():
    bestscore = -100                                # Start with low score
    bestmove = 0                                    # bestmove is 0 to create the variable
    for key in board.keys():                        # for every position on the board do the following: 
        if (board[key] == ' '):                     # If position is empty do the following
            board[key] = player1                    # Place a mark, X in this case since AI is player 1 here 
            score = deepretard1(board, 0, False)    # Check the score of the minimax algorithm
            board[key] = ' '                        # Remove the mark so AI can try other moves for better scores
            if (score > bestscore):                 # If score is higher than last bestscore (AI won more games with that move)     
                bestscore = score                   # Adjust bestscore to see if there are better moves
                bestmove = key                      # Go further with the move with the highest score
    placemove1(player1, bestmove)                   # Place an X on the best position that came out of the algorithm
    return

# DeepRetard marks the board after minimax algorithm if AI is player 2
def compmove2():
    bestscore = -100
    bestmove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = player2
            score = deepretard2(board, 0, False)
            board[key] = ' '
            if (score > bestscore):
                bestscore = score
                bestmove = key
    placemove2(player2, bestmove)
    return

# Deepretard minimax algorithm as player 1
# Plays all possible outcomes of games to see which move is best
# (Plays games against itself)
def deepretard1(board, treedepth, max):
    if (winx()):    				# Checks if win is True
        return 1                    # Gets one point if outcome is postive(won) for deepretard
    elif (wino()):					# Checks if opppent has won
        return -1                   # Loses one point if game outcome is negative(lost) for deepretard
    elif (draw()):					# Checks if the game ends in a draw
        return 0                    # No points when draw
    if (max):                       # If max is True, tries a move, if max is False, tries opponent move
        bestscore = -100            # Score is reset to low
        for key in board.keys():                                 # Tries every position
            if (board[key] == ' '):                              # If empty do the following
                board[key] = player1                             # Place an X
                score = deepretard1(board, treedepth + 1, False) # Every move goes deeper in the tree of possible board states, False to make opponent move next
                board[key] = ' '                                 # Position is reset to empty
                if (score > bestscore):                          # If move is better than the previous best, last move is bestscore
                    bestscore = score                            # Adjust bestscore to see if there are better moves
        return bestscore
    else:
        bestscore = 100                                           # Same thing but for opponent but want to get a score as low as possible
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player2
                score = deepretard1(board, treedepth + 1, True)   # True to make next move for AI again
                board[key] = ' '
                if (score < bestscore):							  #If opponent wins lower the score(bad move)
                    bestscore = score
        return bestscore

# Deepretard minimax algorithm as player 2 
# Plays all possible outcomes of games to see which move is best
def deepretard2(board, treedepth, max):
    if (winx()):
        return -1
    elif (wino()):
        return 1
    elif (draw()):
        return 0
    if (max):
        bestscore = -100
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player2
                score = deepretard2(board, treedepth + 1, False)
                board[key] = ' '
                if (score > bestscore):
                    bestscore = score
        return bestscore
    else:
        bestscore = 100
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player1
                score = deepretard2(board, treedepth + 1, True)
                board[key] = ' '
                if (score < bestscore):
                    bestscore = score
        return bestscore

# Game start
game = 0
art()
print("Enter 1 to play against DeepRetard(c) AI.")
print("Enter 2 to play a 2 player game")
while game not in ['1','2']:
    game = input("Please enter 1 or 2: ")

# 1 player game
if game == '1':
    name1 = input("Please enter your name: ")
    name2 = "DeepRetard"
    print("\nHello "+name1+"!\n")
    print("So you think you can defeat DeepRetard(c)? Good luck!\n")
    manual()
    input("\nPress Enter to see who begins!")
    starter = start()
    if starter == 'p2':
        print("\nDeepRetard(c) begins!")
        boarddraw(board)
        player1 = 'X'
        player2 = 'O'
        
        while not wino() or winx():
            print("Thinking...")
            time.sleep(1)
            print(fun())
            time.sleep(2)
            print(fun2())
            time.sleep(1)
            compmove1()
            print(name1 + ", it's your turn now!\n")
            player2move()
    else:
        print("\nYou begin!")
        boarddraw(board)
        player1 = 'X'
        player2 = 'O'

        while not wino() or winx():
            print(name1+", It's your turn now!\n")
            player1move()
            print("Thinking...")
            time.sleep(1)
            print(fun())
            time.sleep(2)
            print(fun2())
            time.sleep(1)
            compmove2()

# 2 player game
elif game == '2':
    name1 = input("Player 1, please enter your name: ")
    name2 = input("Player 2, please enter your name: ")
    print("\nHello "+name1+" and "+name2+"!\n")
    input("Press Enter to see who begins!")
    starter = start()

    if starter == 'p1':
        print(name1 + " begins!")
        boarddraw(board)
        player1 = 'X'
        player2 = 'O'

        while not wino() or winx():
            
            print(name1+", It's your turn now!\n")
            player1move()
            print(name2+", It's your turn now!\n")
            player2move()
    else:
        print(name2+" begins!")
        boarddraw(board)
        player1 = 'X'
        player2 = 'O'

        while not wino() or winx():
            
            print(name2+", It's your turn now!\n")
            player1move()
            print(name1+", It's your turn now!\n")
            player2move()
