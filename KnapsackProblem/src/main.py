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
    population = init_population(task, POPULATION_SIZE)
    best = get_best_from_population(population)
    print(best.evaluate())
    
def get_best_from_population(population):
    for i in range(ITERATIONS):
        new_population = Population()
        while new_population.population_size < POPULATION_SIZE:
            parent1 = tournament(population, TOURNAMENT_SIZE)
            parent2 = tournament(population, TOURNAMENT_SIZE)
            child = crossover(parent1, parent2, CROSSOVER_RATE)
            mutate(child, MUTATION_RATE)
            new_population.add_individual(child)
        population = new_population
    return population.get_best_individual()

main()