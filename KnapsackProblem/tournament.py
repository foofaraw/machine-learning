import random
from Models.Individual import Individual

def tournament (population, tournament_size):
    sample = random.sample(population.individuals, tournament_size)
    values = []
    for i in sample:
        values.append(i.evaluate())
    
    return sample[values.index(max(values))]

