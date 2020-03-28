import numpy as np
from timeit import default_timer as timer
from Models.Sudoku import Sudoku
from solve import *


def main():
    data = np.genfromtxt('Data/Sudoku.csv', delimiter=';', names=True, dtype=('>i4', '>i4', '|U81', '|U81'))
    sudoku = Sudoku(data[0])

    start = timer()
    solve(sudoku.grid)
    end = timer()

    print('Solved: ' + str(sudoku.is_solved()))
    print('Solution time: ' + str(end - start))

main()