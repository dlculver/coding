import random
import time
boardsize = 100

board = [[random.choice([False, True]) for j in range(boardsize)] for i in range(boardsize)]

#### defining neighbor_count ####
def neighbor_count(i,j):
    result = 0
    if (board[(i-1)%boardsize][j]): result+=1
    if (board[(i-1)%boardsize][(j-1)%boardsize]): result+=1
    if (board[i][(j-1)%boardsize]): result+=1
    if (board[(i+1)%boardsize][(j-1)%boardsize]): result+=1
    if (board[(i+1)%boardsize][j]): result+=1
    if (board[(i+1)%boardsize][(j+1)%boardsize]): result+=1
    if (board[i][(j+1)%boardsize]): result+=1
    if (board[(i-1)%boardsize][(j+1)%boardsize]): result+=1

    return result
################################

############# incorporating rules of the game ############

def iterateGame(i,j):
    if(board[i][j] and (neighbor_count(i,j)==2 or neighbor_count(i,j)==3)): return True
    if(not(board[i][j]) and neighbor_count(i,j)==3): return True
    return False

############ function to run on all cells

def iterateGameWhole():
    boardStore = [[False for j in range(boardsize)] for i in range(boardsize)]
    for i in range(boardsize):
        for j in range(boardsize):
            boardStore[i][j] = iterateGame(i,j)
    return boardStore

##### printing the board ####

def printBoard():
    output = ""
    for i in range(boardsize):
        for j in range(boardsize):
            if(board[i][j]):
                output+="x"
            else:
                output+="o"
        output+="\n"
    print(output)
########################## incorporating time / Main function ############

for k in range(100):
    printBoard()
    board = iterateGameWhole()
    time.sleep(1)
