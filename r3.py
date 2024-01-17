import g_a;

# Define a function to initialize a population of solutions
def initialize_population(population_size, courses, rooms, timeslots):
    # Create a list to store the population
    population = []
    # Iterate over the population size
    for i in range(population_size):
        # Create a schedule and add it to the population
        schedule = create_schedule(courses, rooms, timeslots)
        population.append(schedule)
    # Return the population
    return population

# Define a function to select parents for crossover
def select_parents(population, fitness):
    # Choose two parents randomly from the population
    parent1 = random.choices(population, weights=fitness)[0]
    parent2 = random.choices(population, weights=fitness)[0]
    # Return the parents
    return parent1, parent2

# Define a function to perform crossover
def crossover(parent1, parent2):
    # Choose a random crossover point
    crossover_point = random.randint(1, len(parent1) - 1)
    # Create the child by combining the parents at the crossover point
    child = parent1[:crossover_point] + parent2[crossover_point:]
    # Return the child
    return child

# Define a function to perform mutation
def mutate(schedule, courses, rooms, timeslots):
    # Choose a random exam from the schedule
    exam_index = random.randint(0, len(schedule) - 1)
    # Choose a random room and timeslot for the exam
    room = random.choice(rooms)
    timeslot = random.choice(timeslots)
    # Replace the exam with the new room and timeslot
    schedule[exam_index] = (schedule[exam_index][0], room, timeslot)
    # Return the mutated schedule
    return schedule

