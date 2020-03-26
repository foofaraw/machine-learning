import numpy as np

class Sudoku:
    def __init__(self, data_row):
        self.id = data_row[0]

        # From 0 to 9, 0 being train set with given solutions.
        self.difficulty = data_row[1]

        # 9 rows, each representing one box
        self.grid = self.create_grid(data_row[2])

        # Correctly solved grid for Sudokus with difficulty 0
        self.solution = self.create_solution(data_row[3])
    # 012345678 912345678 9123456789
    def create_grid(self, row):
        row = row.replace('.', '0')
        grid = [row[i:i + 9] for i in range(0, len(row), 9)]
        return np.array(grid)

    def create_solution(self, solution_row):
        return self.create_grid(solution_row) if solution_row else 0

    