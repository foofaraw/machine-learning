import numpy as np

class Sudoku:
    def __init__(self, data_row):
        self.id = data_row[0]

        # From 0 to 9, 0 being train set with given solutions.
        self.difficulty = data_row[1]

        # Array of 9 rows, each row is an array representing one box from Sudoku grid
        # If 0, it needs filling
        self.grid = self.create_grid(data_row[2])

        # Correctly solved grid for Sudokus with difficulty 0
        self.solution = self.create_solution(data_row[3])

    def create_grid(self, row):
        grid = []
        for i in range(9):
            box = np.zeros(9)
            for j in range(9):
                if row[i + j] == '.':
                    box[j] = 0
                else:
                    box[j] = int(row[i + j])
            grid.append(box)
        return np.array(grid, dtype=np.int8)

    def create_solution(self, solution_row):
        if (solution_row):
            return self.create_grid(solution_row)
        else:
            return 0

    