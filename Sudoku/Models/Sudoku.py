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

    def create_grid(self, data_row):
        data_row = data_row.replace('.', '0')
        row_int = [int(i) for i in data_row]
        grid = [row_int[i:i + 9] for i in range(0, len(row_int), 9)]
        return np.array(grid)

    def create_solution(self, solution_row):
        return self.create_grid(solution_row) if solution_row else 0

    def is_solved(self):
        return np.array_equal(self.grid, self.solution)

    