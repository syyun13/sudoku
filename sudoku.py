from random import randrange

# solvable sudoku puzzles
puzzles = [
    [
        [0, 3, 0, 0, 8, 0, 0, 0, 1],
        [0, 0, 7, 4, 0, 1, 0, 5, 0],
        [9, 0, 0, 0, 5, 0, 2, 0, 0],
        [0, 0, 2, 0, 0, 5, 0, 1, 0],
        [3, 0, 0, 2, 1, 0, 5, 0, 0],
        [5, 9, 0, 0, 6, 0, 0, 0, 2],
        [0, 0, 6, 5, 0, 2, 0, 0, 0],
        [0, 0, 9, 6, 0, 0, 0, 2, 7],
        [0, 0, 0, 0, 0, 8, 0, 6, 5]
    ],
    [
        [2, 0, 5, 0, 0, 9, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 3, 0, 7],
        [7, 0, 0, 8, 5, 6, 0, 1, 0],
        [4, 5, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 8, 5],
        [0, 2, 0, 4, 1, 8, 0, 0, 6],
        [6, 0, 8, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 2, 0, 0, 7, 0, 8]
    ],
    [
        [0, 0, 6, 8, 0, 0, 0, 9, 4],
        [0, 2, 0, 0, 6, 0, 7, 0, 0],
        [7, 0, 0, 4, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [6, 4, 0, 0, 2, 8, 3, 5, 0],
        [0, 9, 0, 5, 0, 1, 0, 0, 2],
        [4, 0, 2, 6, 0, 3, 0, 0, 5],
        [0, 0, 0, 0, 1, 0, 0, 0, 3],
        [8, 0, 9, 0, 0, 0, 1, 2, 0]
    ],
    [
        [0, 4, 0, 0, 1, 0, 9, 0, 8],
        [8, 0, 5, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 2, 0, 0, 0, 5, 0, 0, 4],
        [0, 0, 1, 6, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 8, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [3, 0, 4, 0, 0, 0, 8, 0, 0],
        [0, 8, 0, 0, 9, 0, 4, 0, 3]
    ]
]

# print out the sudoku puzzle
def printAll(p):
    for i in range(len(p)):
        # divider after 3 lines
        if i != 0 and i % 3 == 0:
            print("- - - - - - - - - - - - - - -")
        for j in range(0,len(p[i])):
            # divider after 3 numbers
            if j != 0 and j % 3 == 0:
                print("| ", end="")
            # linebreak after the last element
            if j == len(p[i]) - 1:
                print(p[i][j])
            # do not linebreak for others
            else:
                print(p[i][j], " ", end="")

# find an empty cell and return its row and column
def emptyCell(p):
    for i in range(len(p)):
        for j in range(len(p[i])):
            if p[i][j] == 0:
                return i, j
    return False

# check if the sudoku is valid when we plug in "num" at the "col" - "row" position
def validate(p, num, col, row):
    # check if there's a duplicate number in its row/column
    for i in range(len(p)):
        if p[col][i] == num and i != row:
            return False
        if p[i][row] == num and i != col:
            return False
    # find the position of current cell's 3 x 3 area
    x_cell = col // 3 * 3
    y_cell = row // 3 * 3
    # check if there's a duplicate number in its 3 x 3 area
    for x in range(x_cell, x_cell+3):
        for y in range(y_cell, y_cell+3):
            if p[x][y] == num and x != col and y != row:
                return False
    return True

# solve the sudoku
def findAnswer(p):
    if not emptyCell(p):
        return True
    # find an empty cell
    c, r = emptyCell(p)
    # try all numbers 1 ~ 9 in that empty position
    for n in range(1,10):
        if validate(p, n, c, r):
            p[c][r] = n
            if findAnswer(p):
                return True
            # reset the cell to 0 because the number did not work
            else:
                p[c][r] = 0
    return False

# randomly choose 1 puzzle from the list
r = randrange(0,4)
puzzle = puzzles[r]

# print the unsolved sudoku
printAll(puzzle)

print("\n.......... solving ..........\n")
findAnswer(puzzle)

# print the solved answer
printAll(puzzle)