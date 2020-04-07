import matplotlib.pyplot as plt
import numpy as np

from timeit import default_timer as timer
from generate import generate
from read import read
from init_population import init_population
from tournament import tournament
from crossover import crossover
from mutate import mutate
from Models.Population import Population
from Models.Consts import *

def main():
    # generate(NUMBER_OF_ITEMS, MAX_WEIGHT, MAX_SIZE, FILE_NAME)
    task = read(FILE_NAME)
    run_task(task) 
    
def run_task(task):    
    print('Population size: ' + str(POPULATION_SIZE))
    print('Number of generations: ' + str(ITERATIONS))

    start = timer()
    population = init_population(task, POPULATION_SIZE)
    best = get_best_from_population(population)
    end = timer()
    print('Execution time: ' + str(end - start))

    plt.plot(best)
    plt.xlabel('GENERATION')
    plt.ylabel('BEST INDIVIDUAL')
    plt.show()


# Returns np.array 1xITERATIONS of best individual in each generation
def get_best_from_population(population):
    result = np.empty(ITERATIONS)
    for i in range(ITERATIONS):
        new_population = Population()
        while new_population.population_size < POPULATION_SIZE:
            parent1 = tournament(population, TOURNAMENT_SIZE)
            parent2 = tournament(population, TOURNAMENT_SIZE)
            child = crossover(parent1, parent2, CROSSOVER_RATE)
            mutate(child, MUTATION_RATE)
            new_population.add_individual(child)
            print('.', end='')
        population = new_population
        result[i] = population.get_best_individual().evaluate()
        print('-', end='')
    return result

main()