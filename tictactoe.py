symbol = [" ","X","O"]
def printRow(row):
    output = "|"
    for i in range(3):
        output = output + " " + symbol[row[i]] + " |"
    print(output)

def printBoard(board):
    print("+-----------+") 
    for i in range(3):
        printRow(board[i]) 
        print("+-----------+")   
    
def markBoard(board, row, col, player):
    if board[row][col] == 0:
       board[row][col] = player
    else:
        print("Please pick an empty square!")

def getPlayerMove():
    row = int(input("Pick a row (1-3): ")) 
    col = int(input("Pick a column (1-3): "))
    return (row - 1, col - 1) 

def hasBlanks(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return True
    return False
            
def main():
    board = [[0,0,0],
             [0,0,0],
             [0,0,0]]
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row, col = getPlayerMove()
        markBoard(board, row, col, player)
        player = player % 2 + 1
    printBoard(board)
    print("The board is full...")
main()
