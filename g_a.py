import random

solution = [('C1', 'T1', 'H1'), ('C2', 'T2', 'H1'), ('C3', 'T3', 'H1'), 
            ('C4', 'T1', 'H2'), ('C5', 'T2', 'H2'), ('C1', 'T2', 'H2'), 
            ('C2', 'T3', 'H2'), ('C3', 'T1', 'H1'), ('C4', 'T2', 'H1'), 
            ('C5', 'T3', 'H1'), ('C1', 'T3', 'H2'), ('C2', 'T1', 'H2'), 
            ('C3', 'T2', 'H2'), ('C4', 'T3', 'H1'), ('C5', 'T1', 'H1')]


# Define the representation for a solution to the scheduling problem
def create_schedule(courses, rooms, timeslots):
    # Shuffle the rooms and timeslots to add some randomness to the schedule
    random.shuffle(rooms)
    random.shuffle(timeslots)
    # Create a list to store the schedule
    schedule = []
    # Iterate over each course
    for course in courses:
        # Assign the next available room and timeslot to the course
        room = rooms[len(schedule) % len(rooms)]
        timeslot = timeslots[len(schedule) % len(timeslots)]
        # Add the course, room, and timeslot to the schedule
        schedule.append((course, room, timeslot))
    # Return the schedule
    return schedule


# Define a function to calculate the fitness of a solution
def calculate_fitness(schedule, conflicts):
    # Initialize the fitness score to 0
    fitness = 0
    # Iterate over each pair of exams
    for i in range(len(schedule)):
        for j in range(i + 1, len(schedule)):
            # Check if the exams have conflicting students
            if (schedule[i][0], schedule[j][0]) in conflicts:
                # Check if the exams are scheduled at the same time
                if schedule[i][2] == schedule[j][2]:
                    # If they are, increment the fitness score
                    fitness += 1
    # Return the fitness score
    return fitness


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
    # Choose a random timeslot for the exam
    timeslot = random.choice(timeslots)
    # Replace the exam with the new timeslot
    schedule[exam_index] = (schedule[exam_index][0], schedule[exam_index][1], timeslot)
    # Return the mutated schedule
    return schedule
