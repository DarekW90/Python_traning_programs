def findNextEmpty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None

def isValid(puzzle, guess,row,col):
    rowVals = puzzle[row]
    if guess in rowVals:
        return False
    
    #colVals = []
    #for i in range(9):
    #    colVals.append(puzzle[i][col])
    colVals = [puzzle[i][col] for i in range(9)]
    if guess in colVals:
        return False
    
    rowStart = (row//3)*3
    colStart = (col//3)*3
    
    for r in range(rowStart, rowStart + 3):
        for c in range(colStart, colStart + 3):
            if puzzle[r][c] == guess:
                return False
            
    return True

def solveSudoku(puzzle):
    row,col = findNextEmpty(puzzle)
    
    if row is None:
        return True
    
    for guess in range(1,10):
        if isValid(puzzle, guess,row,col):
            puzzle[row][col] = guess
            if solveSudoku(puzzle):
                return True
            
        puzzle[row][col] = -1
    
    return False

if __name__ == '__main__':
    exampleBoard = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solveSudoku(exampleBoard))
    print(exampleBoard)