import numpy as np
from Models.Consts import CROSSOVER_POINT
from Models.Individual import Individual

def crossover(parent1, parent2, crossover_rate):
    if (np.random.uniform(0, 1) < crossover_rate):
        child_items = parent1.items[:CROSSOVER_POINT] + parent2.items[-(len(parent1.items) - CROSSOVER_POINT):]
        return Individual(child_items, parent1.task)
    else:
        return parent1
    
