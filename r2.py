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
