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

# Implement a local search algorithm to improve the quality of a solution
def local_search(individual):
    best_fitness = fitness(individual)
    improved = True
    while improved:
        improved = False
        for i in range(len(individual)):
            for j in range(i+1, len(individual)):
                temp = individual[:]
                temp[i], temp[j] = temp[j], temp[i]
                new_fitness = fitness(temp)
                if new_fitness < best_fitness:
                    individual = temp
                    best_fitness = new_fitness
                    improved = True
    return individual

# Implement the genetic algorithm with local search

# Implement the genetic algorithm with local search
def genetic_algorithm(population_size, generations, selection_size, mutation_rate):
    # Create an initial population
    population = create_population(population_size)

    # Evolve the population over multiple generations
    for i in range(generations):
        # Select parents for crossover
        parents = selection(population, selection_size)

        # Generate offspring through crossover and mutation
        offspring = []
        for j in range(population_size - selection_size):
            parent1 = random.choice(parents)
            parent2 = random.choice(parents)
            child = crossover(parent1, parent2)
            if random.random() < mutation_rate:
                child = mutation(child)
            offspring.append(child)

        # Evaluate fitness of offspring
        offspring_fitness = [fitness(individual) for individual in offspring]

        # Select survivors for the next generation
        combined_population = population + offspring
        fitness_scores = [fitness(individual) for individual in combined_population]
        sorted_population = [x for _, x in sorted(zip(fitness_scores, combined_population))]
        population = sorted_population[:population_size]

        # Perform local search on a randomly selected individual
        individual_idx = random.randint(0, population_size - 1)
        original_individual = population[individual_idx]
        new_individual = local_search(original_individual)
        new_fitness = fitness(new_individual)
        if new_fitness < fitness(original_individual):
            population[individual_idx] = new_individual

    # Return the best solution found
    fitness_scores = [fitness(individual) for individual in population]
    best_individual = population[fitness_scores.index(min(fitness_scores))]
    return best_individual

# Perform local search on an individual
def local_search(individual):
    # Randomly choose a course to move
    course_idx = random.randint(0, len(COURSES) - 1)
    original_exam = individual[course_idx]

    # Try moving the course to a new time slot and/or exam hall
    best_exam = original_exam
    best_fitness = fitness(individual)
    for time_slot in TIME_SLOTS:
        for exam_hall in EXAM_HALLS:
            new_exam = (original_exam[0], time_slot, exam_hall)
            new_individual = individual.copy()
            new_individual[course_idx] = new_exam
            new_fitness = fitness(new_individual)
            if new_fitness < best_fitness:
                best_exam = new_exam
                best_fitness = new_fitness

    # Update the individual with the best move
    new_individual = individual.copy()
    new_individual[course_idx] = best_exam
    return new_individual
