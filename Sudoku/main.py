import numpy as np
from Models.Sudoku import Sudoku
from solve import *


def main():
    data = np.genfromtxt('Data/Sudoku.csv', delimiter=';', names=True, dtype=('>i4', '>i4', '|U81', '|U81'))
    sudoku = Sudoku(data[0])
    res = solve(sudoku.grid)
    print(res)

main()