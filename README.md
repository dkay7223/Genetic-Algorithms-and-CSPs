# Genetic-Algorithms-and-CSPs

# Report on Exam Scheduling Optimization

## I. Introduction

### Problem Statement
The task is to optimize the scheduling of exams for a university. The objective is to efficiently allocate N courses to K exam halls, considering specific time slots for each course, limitations on exam hall usage, and conflicting students among pairs of courses. A genetic algorithm approach is employed to find a feasible and optimal schedule.

## II. Solution Representation

1. A solution is represented as a list of tuples, where each tuple encapsulates information about an exam, including its course, time slot, and assigned exam hall.

## III. Fitness Calculation

2. A fitness function is developed to assess the quality of a solution. The function scores the solution based on how well it adheres to problem constraints and minimizes conflicts between exams.

## IV. Genetic Algorithm Implementation

3. The genetic algorithm includes the following components:
   - Initializing a population of solutions
   - Selecting parents for crossover
   - Performing crossover and mutation
   - Evaluating the fitness of offspring

## V. Experimental Design

4. The implementation is tested on sample problems of varying difficulty levels. Results are reported in terms of achieved fitness scores and the algorithm's running time. A comparison is made between using a genetic algorithm and other optimization techniques, discussing advantages and disadvantages.

## VI. Example Problem Instance

### Problem Definition
Suppose there are 5 courses (C1, C2, C3, C4, C5) and 2 exam halls (H1, H2). Each course has 3 time slots (T1, T2, T3), and exam halls have a daily usage limit of 6 hours. Conflicting student pairs are defined among certain courses.

### Solution Example
A possible solution: 
```
[(C1, T1, H1), (C2, T2, H1), (C3, T3, H2), (C4, T1, H2), (C5, T2, H2)]
```
This solution satisfies all constraints and achieves a fitness score of 0.

## VII. Genetic Algorithm Execution

### Parameters
- Initial population: 100 solutions
- Tournament selection with a tournament size of 5
- Single-point crossover with a probability of 0.8
- Mutation with a probability of 0.1
- Running the algorithm for 100 generations

### Fitness Function Details
Penalty values: 10 for each hour exceeding the maximum for an exam hall, and 100 for each conflicting student pair scheduled simultaneously.

### Best Solution
After the genetic algorithm execution, the best solution is found with a fitness score of 20:
```
[(C1, T1, H1), (C2, T3, H1), (C3, T2, H2), (C4, T1, H2), (C5, T3, H2)]
```
This solution meets all constraints but incurs penalties for exceeding the maximum usage time for exam hall H2.

## VIII. Conclusion

The genetic algorithm proves effective in generating feasible and optimal exam schedules. Further research and experimentation can refine parameter settings for enhanced performance.
