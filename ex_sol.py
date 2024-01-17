class Exam:
    def __init__(self, course, time_slot, exam_hall):
        self.course = course
        self.time_slot = time_slot
        self.exam_hall = exam_hall
        
class Schedule:
    def __init__(self, exams):
        self.exams = exams
    
    def __getitem__(self, index):
        return self.exams[index]
    
    def __setitem__(self, index, exam):
        self.exams[index] = exam
        
    def __len__(self):
        return len(self.exams)
    
    def fitness_score(self, halls, conflicts):
        score = 0
        for exam in self.exams:
            # Check if exam hall usage limit is exceeded
            if exam.exam_hall in halls:
                hall_time = halls[exam.exam_hall]
                if exam.time_slot[1] > hall_time:
                    score += (exam.time_slot[1] - hall_time) * 10
        
            # Check for conflicts with other exams
            for conflict in conflicts:
                if exam.course == conflict[0]:
                    for other_exam in self.exams:
                        if other_exam.course == conflict[1] and \
                           exam.time_slot[0] < other_exam.time_slot[1] and \
                           exam.time_slot[1] > other_exam.time_slot[0]:
                            score += 100
                            break
        return score

def generate_population(courses, time_slots, exam_halls, size):
    population = []
    for i in range(size):
        exams = []
        for course in courses:
            exam = Exam(course, random.choice(time_slots), random.choice(exam_halls))
            exams.append(exam)
        population.append(Schedule(exams))
    return population

def tournament_selection(population, k):
    tournament = random.sample(population, k)
    return max(tournament, key=lambda x: x.fitness_score())

def single_point(parent1, parent2):
    # choose a random crossover point
    crossover_point = random.randint(0, len(parent1)-1)

    # swap the tails of the parents' gene sequences
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]

    return offspring1, offspring2

def mutation(solution):
    # choose a random gene
    gene_index = random.randint(0, len(solution)-1)
    gene = solution[gene_index]

    # assign a new value to the gene
    new_time_slot = random.choice(TIME_SLOTS)
    new_exam_hall = random.choice(EXAM_HALLS)
    new_gene = (gene[0], new_time_slot, new_exam_hall)

    # replace the gene in the solution
    new_solution = solution[:gene_index] + (new_gene,) + solution[gene_index+1:]

    return new_solution

def genetic_algorithm(pop_size, num_generations):
    # initialize the population of solutions
    population = [generate_solution() for i in range(pop_size)]
    best_solution = None
    best_fitness = float('inf')

    # run the algorithm for the specified number of generations
    for gen in range(num_generations):
        # evaluate the fitness of each solution
        fitness_scores = [fitness(solution) for solution in population]

        # select the parents for crossover
        parents = [tournament_selection(population, fitness_scores) for i in range(pop_size)]

        # generate offspring solutions through crossover and mutation
        offspring = []
        for i in range(0, pop_size, 2):
            parent1 = parents[i]
            parent2 = parents[i+1]
            if random.random() < CROSSOVER_PROBABILITY:
                child1, child2 = single_point(parent1, parent2)
            else:
                child1, child2 = parent1, parent2
            if random.random() < MUTATION_PROBABILITY:
                child1 = mutation(child1)
            if random.random() < MUTATION_PROBABILITY:
                child2 = mutation(child2)
            offspring.append(child1)
            offspring.append(child2)

        # replace the old population with the offspring population
        population = offspring

        # update the best solution found so far
        for solution in population:
            solution_fitness = fitness(solution)
            if solution_fitness < best_fitness:
                best_fitness = solution_fitness
                best_solution = solution

        # print the best solution found so far
       


# print("Best solution found: ", best_solution)
# print("Fitness score: ", best_fitness)

# # extract the schedule from the best solution
# schedule = [exam for exam, timeslot, hall in best_solution]

# # print the schedule
# print("Exam Schedule:")
# for i in range(len(schedule)):
#     print(f"{schedule[i]}: {timeslots[i % len(timeslots)]}, {halls[i % len(halls)]}")



