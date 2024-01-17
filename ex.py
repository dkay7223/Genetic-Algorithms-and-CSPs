import random

# Constants defining the problem instance
COURSES = ['C1', 'C2', 'C3', 'C4', 'C5']
EXAM_HALLS = ['H1', 'H2']
TIME_SLOTS = ['T1', 'T2', 'T3']

CONFLICTS = {
    ('C1', 'C2'): 10,
    ('C1', 'C4'): 5,
    ('C2', 'C5'): 7,
    ('C3', 'C4'): 12,
    ('C4', 'C5'): 8
}

# Define a solution representation as a list of tuples
# Each tuple represents an exam and contains information about its course,
# time slot, and exam hall.
def create_individual():
    individual = []
    for course in COURSES:
        exam = (
            course,
            random.choice(TIME_SLOTS),
            random.choice(EXAM_HALLS)
        )
        individual.append(exam)
    return individual

# Create a population of individuals
def create_population(population_size):
    population = []
    for i in range(population_size):
        population.append(create_individual())
    return population

# Calculate the fitness of an individual
def fitness(individual):
    conflicts = 0
    for i in range(len(COURSES)):
        for j in range(i+1, len(COURSES)):
            course1, time1, hall1 = individual[i]
            course2, time2, hall2 = individual[j]
            if course1 != course2 and (course1, course2) in CONFLICTS:
                if time1 == time2 and hall1 == hall2:
                    conflicts += CONFLICTS[(course1, course2)]
    return conflicts

# Select parents for crossover
def selection(population, k):
    return random.sample(population, k)

# Combine two parents to create a new offspring
def crossover(parent1, parent2):
    point = random.randint(1, len(COURSES) - 1)
    offspring = parent1[:point] + parent2[point:]
    return offspring

# Introduce random changes in an individual to increase diversity
def mutation(individual):
    gene = random.randint(0, len(COURSES) - 1)
    individual[gene] = (
        individual[gene][0],
        random.choice(TIME_SLOTS),
        random.choice(EXAM_HALLS)
    )
    return individual

# Implement the genetic algorithm
def genetic_algorithm(population_size, generations, selection_size, mutation_rate):
    # Create an initial population
    population = create_population(population_size)

    # Evolve the population over multiple generations
    for i in range(generations):
        # Select parents for crossover
        parents = selection(population, selection_size)

