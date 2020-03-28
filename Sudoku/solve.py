import numpy as np

def solve(grid):
    find = find_empty(grid)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(grid, i, row, col):
            grid[row][col] = i

            if solve(grid):
                return True

            grid[row][col] = 0

    return False    

def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def is_valid(grid, num, row, col):
    for i in range(9):
        # check row
        if grid[row][i] == num and col != i:
            return False

        # check column
        if grid[i][col] == num and row != i:
            return False

    # Check box
    box_x = (col // 3) * 3
    box_y = (row // 3) * 3

    for i in range(box_y, box_y + 3):
        for j in range(box_x, box_x + 3):
            if grid[i][j] == num and (i, j) != (row, col):
                return False

    return True