import random
import numpy as np

seed_value = 15
random.seed(seed_value)
np.random.seed(seed_value)

items = [
    [4,20],
    [2,60],
    [6,35],
    [1,50],
    [8,40]
]

knapsack_capacity = 15
mutation_rate = 0.1
population_size = 6
chromosome_length = 5
crossover_rate = 0.7
generations = 50

def initilize_population():
    population = []
    for i in range(population_size):
        chromosome = []
        for j in range(chromosome_length):
            chromosome.append(random.randint(0,1))
        population.append(chromosome)
    return population

def fitness_function(chromosome):
    total_weights = 0
    total_values = 0
    for i in range(len(chromosome)):
        if chromosome[i] == 1:
            total_weights += items[i][0]
            total_values += items[i][1]
    if total_weights <= 15:
        return total_values
    return 0

def calculating_fitness(population):
    fitness_population = []
    for i in range(population_size):
        fitness_population.append(fitness_function(population[i]))
    return fitness_population

def selecting_parents(population, fitness):
    total_fitness = sum(fitness)
    selection_probabiities = []
    for i in fitness:
        selection_probabiities.append(i/total_fitness)
    
    parent1 = population[np.random.choice(len(population),p=selection_probabiities)]
    parent2 = population[np.random.choice(len(population),p=selection_probabiities)]

    return parent1,parent2

def crossover(parent1,parent2):
    crossover_point = random.randint(0,len(parent1))
    if np.random.rand() < crossover_rate:
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent1[crossover_point:] + parent2[:crossover_point]
        return child1,child2
    return parent1,parent2
    
     
def mutate(chrmosome):
    mutated_chromosome = []
    for i in chrmosome:
        if np.random.rand() < mutation_rate:
            mutated_chromosome.append(1-i)
        else:
            mutated_chromosome.append(i)
    return mutated_chromosome 

def genetic_algo():
    population = initilize_population()
    for generation in range(generations):
        fitness = calculating_fitness(population)   
        print(f"\nGeneration {generation + 1}:")
        for i, chromosome in enumerate(population):
            print(f"Chromosome {i + 1}: {chromosome}, Fitness: {fitness[i]}")

        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = selecting_parents(population, fitness)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)

            new_population.append(child1)
            if len(new_population) < population_size:
                new_population.append(child2)

        population = new_population
 
        best_fitness = max(fitness)
        print(f"Best Fitness in Generation {generation + 1}: {best_fitness}")

    print("\nFinal Population:")
    for i, chromosome in enumerate(population):
        print(f"Chromosome {i + 1}: {chromosome}, Fitness: {fitness_function(chromosome)}")

    fitness = calculating_fitness(population)
    best_index = fitness.index(max(fitness))
    best_solution = population[best_index]

    print("\nBest solution found:")
    print("Chromosome:", best_solution)
    print("Value:", fitness_function(best_solution))

genetic_algo()
