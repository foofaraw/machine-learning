from generate import generate
from read import read
from init_population import init_population
from tournament import tournament
from crossover import crossover
from Models.Consts import *

def main():
    # generate(NUMBER_OF_ITEMS, MAX_WEIGHT, MAX_SIZE, FILE_NAME)
    task = read(FILE_NAME)
    population = init_population(task, POPULATION_SIZE)

    for individual in population.individuals:
        sum = individual.evaluate()
        print(sum)
    
    winner1 = tournament(population, TOURNAMENT_SIZE)
    winner2 = tournament(population, TOURNAMENT_SIZE)
    child = crossover(winner1, winner2, CROSSOVER_RATE)
    print('Done')

main()