import numpy as np

def find_empty(grid):
    for i in range(grid.size):
        for j in range(grid[0].size):
            if grid[i][j] == 0:
                return (i, j)
    return None

def is_valid(grid, digit, x, y):
    # Check row
    for i in range(9):
        if grid[x][i] == digit and y != i:
            return False

    # Check column
    for i in range(9):
        if grid[i][y] == digit and x != i:
            return False

    # Check box
    box_x = y // 3
    box_y = x // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == digit and (i, j) != (x, y):
                return False

    return True