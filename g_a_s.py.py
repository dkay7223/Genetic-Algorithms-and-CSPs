import random

# Define the problem instance
N = 6
K = 3
hall_max_hours = 7
time_slots = ['T1', 'T2', 'T3','T4']
exam_halls = ['H1', 'H2']
conflicts = [('C1', 'C2'), ('C2', 'C5'), ('C2', 'C6'), ('C3', 'C4'),('C4','C5')]

# Define the fitness function
def fitness(schedule):
    score = 0
    for exam, time_slot, hall in schedule:
        # Check hall usage
        hall_hours = sum([1 for e, t, h in schedule if h == hall])
        if hall_hours > hall_max_hours:
            # Penalty for exceeding hall usage
            score += 10 * abs(hall_hours - hall_max_hours)
        # Check conflicts
        for c1, c2 in conflicts:
            if exam == c1:
                if any([e == c2 and t == time_slot for e, t, h in schedule]):
                    # Penalty for conflicting exams
                    score += 100
        # Check if two different exams are scheduled at the same time and in the same hall
        if len([1 for e, t, h in schedule if e != exam and t == time_slot and h == hall]) > 0:
            # Penalty for scheduling different exams in same hall at the same time
            score += 1000
    return score

# Define the genetic algorithm
def genetic_algorithm(pop_size, num_generations):
    # Initialize population
    population = []
    for i in range(pop_size):
        schedule = []
        # Initialize hall occupancy
        occupied = {(t, h): False for t in time_slots for h in exam_halls}
        # Schedule exams randomly
        for j in range(N):
            exam = 'C' + str(j+1)
            available_slots = [t for t in time_slots if not any([(exam, t, h) in schedule for h in exam_halls])]
            available_halls = [h for h in exam_halls if not any([(exam, t, h) in schedule for t in time_slots])]
            time_slot = random.choice(available_slots)
            hall = random.choice(available_halls)
            schedule.append((exam, time_slot, hall))
            # Update hall occupancy
            occupied[(time_slot, hall)] = True
        population.append(schedule)
    # Evolve population
    for gen in range(num_generations):
        # Select parents using tournament selection
        parents = []
        for i in range(pop_size):
            tournament = random.sample(population, 5)
            tournament_fitness = [fitness(s) for s in tournament]
            winner = tournament[tournament_fitness.index(min(tournament_fitness))]
            parents.append(winner)
        # Apply crossover
        offspring = []
        for i in range(0, pop_size, 2):
            p1 = parents[i]
            p2 = parents[i+1]
            if random.random() < 0.8:
                # Perform crossover
                crossover_point = random.randint(1, N-1)
                child1 = p1[:crossover_point] + p2[crossover_point:]
                child2 = p2[:crossover_point] + p1[crossover_point:]
                offspring.extend([child1, child2])
            else:
                # If no crossover, just add parents to offspring
                offspring.extend([p1, p2])
        # Apply mutation
        for i in range(pop_size):
            if random.random() < 0.1:
                schedule = offspring[i]
                exam, time_slot, hall = random.choice(schedule)
                new_time_slot = random.choice([t for t in time_slots if t != time_slot])
                new_hall = random.choice([h for h in exam_halls if h != hall])
                offspring[i][offspring[i].index((exam, time_slot, hall))] = (exam, new_time_slot, new_hall)
        # Replace population with offspring
        population = offspring
    # Find best solution
    best_schedule = min(population, key=fitness)
    return best_schedule

# Run the genetic algorithm
best_schedule = genetic_algorithm(pop_size=100, num_generations=100)
print(best_schedule)
print(fitness(best_schedule))
