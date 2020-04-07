class Population:
    def __init__(self, individuals=[], size=0):
        self.individuals = individuals
        self.population_size = size

    def add_individual(self, individual):
        self.individuals.append(individual)
        self.population_size = self.population_size + 1

    def get_best_individual(self):
        values = []
        for i in self.individuals:
            values.append(i.evaluate())
        
        best_index = values.index(max(values))
        return self.individuals[best_index]

