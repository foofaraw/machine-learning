import numpy as np
from Models.Individual import Individual

def crossover(parent1, parent2, crossover_rate):
    if (np.random.uniform(0, 1) < crossover_rate):
        crossover_point = np.random.randint(1, len(parent1.items) - 1)
        child_items = parent1.items[:crossover_point] + parent2.items[-(len(parent1.items) - crossover_point):]
        return Individual(child_items, parent1.task)
    else:
        return parent1
    
