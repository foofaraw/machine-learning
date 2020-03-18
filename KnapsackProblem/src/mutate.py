import random

def mutate(individual, mutation_rate):
    number_of_genes = individual.number_of_items * mutation_rate
    pos = random.sample(range(0, individual.number_of_items), number_of_genes)
    for i in pos:
        individual.items[i] = not individual.items[i]
