symbol = [" ","X","O"]
def printRow(row):
    output = "|" #initialize output to the left border
    for i in range(3): # for each square in the row
        output = output + " " + symbol[row[i]] + " |" # add to output the symbol for this square followed by a border
    print(output) # print the completed output for this row

def printBoard(board):
    print("+-----------+") # print the top border
    for i in range(3):
        printRow(board[i]) # for each row in the board
        print("+-----------+") # print the row, print the next border    
    
def markBoard(board, row, col, player):
    if i in board == 0: # check to see whether the desired square is blank
        column = # if so, set it to the player number

def getPlayerMove():
    row = input(int("Pick a row (1-3): ")) # prompt user separately for the row and column numbers
    column = input(int("Pick a column (1-3): "))
    return (row - 1, column - 1) # then return that row and column instead of (0,0)

def hasBlanks(board):
    # for each row in the board
    # for each square in the row
    # check whether the square is blank
    # if so, return True
    return True # if no square is blank, return False

def main():
    board = [[0,0,0],
             [0,0,0],
             [0,0,0]] # TODO replace this with a 3x3 matrix of zero's
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row, col = getPlayerMove()
        markBoard(board, row, col, player)
        player = player % 2 + 1 # switch player for next turn

main()
