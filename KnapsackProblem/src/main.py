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

    for j in range(5):
        print('########## NEW RUN ##########')
        population = init_population(task, POPULATION_SIZE)
        start = timer()
        best = get_best_from_population(population)
        end = timer()
        print('# Execution time: ' + str(end - start))
    
def get_best_from_population(population):
    val_sum = 0
    for i in range(ITERATIONS):
        new_population = Population()
        while new_population.population_size < POPULATION_SIZE:
            parent1 = tournament(population, TOURNAMENT_SIZE)
            parent2 = tournament(population, TOURNAMENT_SIZE)
            child = crossover(parent1, parent2, CROSSOVER_RATE)
            mutate(child, MUTATION_RATE)
            new_population.add_individual(child)
        population = new_population
        best_in_generation = population.get_best_individual().evaluate()
        print('Best in ' + str(i + 1) + ' generation: ' + str(best_in_generation))
    return population.get_best_individual()

main()