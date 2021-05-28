import pygame

pygame.init()

screen = pygame.display.set_mode((560, 600))
pygame.display.set_caption("sudoku")

font = pygame.font.SysFont(None, 50)
button_font = pygame.font.SysFont(None, 20)

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
    ]
]

puzzle_i = 0
board = puzzles[puzzle_i]

# draw sudoku board's grids
def sudoku_board():
    screen.fill(pygame.Color("white"))
    pygame.draw.rect(screen, pygame.Color("black"), pygame.Rect(10,10,540,540), 3)
    n = 60
    while n < 540:
        if n == 180 or n == 360:
            weight = 3
        else:
            weight = 1
        pygame.draw.line(screen, pygame.Color("black"), pygame.Vector2(n + 10, 10), pygame.Vector2(n + 10, 550), weight)
        pygame.draw.line(screen, pygame.Color("black"), pygame.Vector2(10, n + 10), pygame.Vector2(550, n + 10), weight)
        n += 60

# fill numbers into the sudoku board
def fill_sudoku():
    for i in range(len(board)):
        for j in range(len(board[0])):
            # blank space when the cell is 0
            n = " " if board[i][j] == 0 else str(board[i][j])
            num = font.render(n, True, pygame.Color("black"))
            screen.blit(num, pygame.Vector2(j*60 + 30, i*60 + 27))

# draw arrows and text at the bottom of the screen
def draw_bottom():
    prev = font.render("<<", True, pygame.Color("black"))
    screen.blit(prev, pygame.Vector2((7, 555)))

    next = font.render(">>", True, pygame.Color("black"))
    screen.blit(next, pygame.Vector2((510, 555)))

    solve = font.render("PRESS SPACE TO SOLVE", True, pygame.Color("black"))
    screen.blit(solve, pygame.Vector2((70, 560)))

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
            # overwrite the number on screen
            num = font.render(str(n), True, pygame.Color("black"), pygame.Color("white"))
            screen.blit(num, pygame.Vector2(r*60 + 30, c*60 + 27))
            pygame.display.update()
            pygame.time.delay(100)
            if findAnswer(p):
                return True
            # reset the cell to 0 because the number did not work
            else:
                # overwrite the number on screen with white so that it is back to empty cell
                num = font.render(str(p[c][r]), True, pygame.Color("white"), pygame.Color("white"))
                p[c][r] = 0
                screen.blit(num, pygame.Vector2(r*60 + 30, c*60 + 27))
                pygame.display.update()
                pygame.time.delay(100)
    return False

play = True

while play:

    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            # change to previous puzzle
            if event.key == pygame.K_LEFT:
                if puzzle_i == 0:
                    puzzle_i = len(puzzles) - 1
                else:
                    puzzle_i -= 1
                board = puzzles[puzzle_i]
                fill_sudoku()
            # change to next puzzle
            if event.key == pygame.K_RIGHT:
                if puzzle_i == len(puzzles) - 1:
                    puzzle_i = 0
                else:
                    puzzle_i += 1
                board = puzzles[puzzle_i]
                fill_sudoku()
            # solve when spacebar is pressed
            if event.key == pygame.K_SPACE:
                findAnswer(board)

    pygame.display.flip()

    sudoku_board()
    draw_bottom()
    fill_sudoku()

pygame.quit()