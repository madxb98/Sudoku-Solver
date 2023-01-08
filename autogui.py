#checks if a number can be placed in a specific position on the grid
def possible(grid, row,column,n):
    #checking the rows
    for i in range(9):
        if grid[row][i] == n:
            return False
    
    #checking the columns
    for i in range(9):
        if grid[i][column] == n:
            return False

    #checking the box n is inside of
    x0 = row - column % 3
    y0 = column - column % 3
    for i in range(3):
        for j in range(3):
            if grid[y0+i][x0+j] == n:
                return False
    return True

#backtracking and solving
def solve(grid, row, column):
    if column == 9:
        if row == 8:
            return True
        row += 1
        column = 0

    if grid[row][column] > 0:
        return solve(grid, row, column + 1)

    for n in range(1,10):
        if possible(grid, row, column, n):
            grid[row][column] = n
            if solve(grid, row, column + 1):
                return True
        grid[row][column] = 0
    return False

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,0,1,9,0,0,5],
        [0,0,0,0,0,0,0,0,0]]

if solve(grid,0,0):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()
else:
    print("no solutions")

