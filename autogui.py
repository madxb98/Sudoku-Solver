import numpy as np

#sudoku board
#this one is an example board to try - want to implement ability to import lists later
grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],[0, 1, 0, 0, 0, 4, 0, 0, 0],[4, 0, 7, 0, 0, 0, 2, 0, 8],[0, 0, 5, 2, 0, 0, 0, 0, 0],[0, 0, 0, 0, 9, 8, 1, 0, 0],[0, 4, 0, 0, 0, 3, 0, 0, 0],[0, 0, 0, 3, 6, 0, 0, 7, 2],[0, 7, 0, 0, 0, 0, 0, 0, 3],[9, 0, 3, 0, 0, 0, 6, 0, 4]]

#checks if a number can be placed in a specific position on the grid
def possible(grid,n,pos):
    #checking the rows
    for i in range(len(grid[0])):
        if grid[pos[0]][i] == n and i != pos[1]:
            return False
    
    #checking the columns
    for i in range(len(grid)):
        if grid[i][pos[1]] == n and i != pos[0]:
            return False

    #checking the box n is inside of
    x0 = (pos[0]//3)*3
    y0 = (pos[1]//3)*3
    for X in range(x0,x0+3):
        for Y in range(y0,y0+3):
            if grid[X][Y] == n and (X,Y) != pos:
                return False
    return True

#finding empty spots on the grid
def find_empty(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                return (row,col)
    return None

#printing the grid
def print_grid(grid):
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("-----------------")
        
        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")

#backtracking and solving
def solve(grid):
    find = find_empty(grid)
    if not find:
        return True
    else:
        row,col = find
    
    for i in range(1,10):
        if possible(grid,i,(row,col)):
            grid[row][col] = i
            if solve(grid):
                return True
            grid[row][col] = 0
    return False

print_grid(grid)
solve(grid)
print("_________________")
print_grid(grid)

