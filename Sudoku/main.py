import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer

from Models.Sudoku import Sudoku
from solve import *

def main():
    data = np.genfromtxt('Data/Sudoku.csv', delimiter=';', names=True, dtype=('>i4', '>i4', '|U81', '|U81'))
    sudokus = [Sudoku(i) for i in data]

    times = []
    sudokus = sudokus[:4]
    for sudoku in sudokus:
        start = timer()
        solve(sudoku.grid, sudoku.domain)
        print(str(sudoku.is_solved()))
        end = timer()
        times.append(end - start)

    x = np.linspace(1, len(sudokus), len(sudokus))
    y = times
    for xx, yy in zip(x, y):
        label = '{:.2f}'.format(yy)
        plt.annotate(label, (xx,yy), textcoords='offset points', xytext=(0,10), ha='center')

    plt.scatter(x, y)
    plt.xticks(np.arange(min(x), max(x) + 1, 1))
    plt.title('Time to solve')
    plt.xlabel('Puzzle no.')
    plt.ylabel('Time (s)')
    plt.show()

main()