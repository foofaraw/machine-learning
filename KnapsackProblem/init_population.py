import numpy as np
from Models.Individual import Individual
from Models.Population import Population
from Models.Consts import PACKING_RATE

def init_population(task, size):
    n_items = int(task.number_of_items)
    individuals = []
    for _ in range(size):
        arr = []
        for _ in range(n_items):
            arr.append(np.random.uniform(0, 1) < PACKING_RATE)
        individual = Individual(arr, task)
        individuals.append(individual)

    return Population(individuals, n_items)