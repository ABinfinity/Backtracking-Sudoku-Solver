from pprint import pprint

def nextEmptyCell(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c   
    return None,None

def isValidMove(puzzle,guess,row,col):
    #checking row
    rowVals = puzzle[row]
    if guess in rowVals:
        return False

    #checking column
    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])
    colVals = [puzzle[i][col] for i in range(9)]
    if guess in colVals:
        return False

    #checking 3x3 grid
    rowStart = (row // 3)*3
    colStart = (col // 3)*3

    for r in range(rowStart, rowStart+3):
        for c in range(colStart, colStart+3):
            if puzzle[r][c] == guess:
                return False
    return True

def solveSudoku(puzzle):
    row,col = nextEmptyCell(puzzle)

    if row is None:
        return True
    
    for guess in range(1,10):
        if isValidMove(puzzle,guess,row,col):
            puzzle[row][col] = guess

            if solveSudoku(puzzle):
                return True
    
        puzzle[row][col] = -1
    return False

if __name__ == '__main__':
    puzzleBoard = [
        [-1,-1 -1,    9, 2, 1,    3, 7, 8],
        [ 8, 7, 9,    3, 4, 5,    1, 2, 6],
        [-1, -1, 1,   8, 6, 7,   -1,-1,-1],

        [4, -1, -1,   -1,-1, 3,   -1, 6,  9],
        [-1,-1, -1,   -1, 1, 4,    7, 8, -1],
        [-1, -1, 5,   -1, 7,-1,   -1,-1, -1],

        [ -1, 5, 3,   -1, -1,-1,   -1, 1,  7],
        [-1,-1, -1,   -1, -1, 6,   9, -1, -1],
        [ 7, 9, -1,   -1,  3,-1,   -1, -1,-1]
    ]
    print(solveSudoku(puzzleBoard))
    pprint(puzzleBoard)