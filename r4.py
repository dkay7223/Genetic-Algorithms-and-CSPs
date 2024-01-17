# Step 4: Test the implementation on sample problems

# Sample exam scheduling problems
problem1 = {
    'num_courses': 4,
    'num_halls': 2,
    'course_slots': {
        1: [1, 2],
        2: [2, 3],
        3: [3, 4],
        4: [1, 3]
    },
    'hall_hours': [3, 4],
    'conflicts': [(1, 2), (2, 3)]
}

problem2 = {
    'num_courses': 5,
    'num_halls': 3,
    'course_slots': {
        1: [1, 3],
        2: [2, 4],
        3: [3, 5],
        4: [4, 6],
        5: [1, 6]
    },
    'hall_hours': [4, 5, 6],
    'conflicts': [(1, 2), (2, 3), (4, 5)]
}

# Test the genetic algorithm on the sample problems
print("Running genetic algorithm on problem 1...")
best_solution, best_fitness = run_genetic_algorithm(problem1)
print("Best solution found:", best_solution)
print("Best fitness found:", best_fitness)

print("Running genetic algorithm on problem 2...")
best_solution, best_fitness = run_genetic_algorithm(problem2)
print("Best solution found:", best_solution)
print("Best fitness found:", best_fitness)
