
import random

# Fitness function
def fitness(x):
    return -x**2 + 10*x + 5

# Genetic Algorithm
def genetic_algorithm():

    # Parameters
    pop_size = 10
    crossover_rate = 0.8
    mutation_rate = 0.1
    generations = 100
    patience = 15

    x_min = 0
    x_max = 10

    # Generate initial random population
    population = [
        random.uniform(x_min, x_max)
        for _ in range(pop_size)
    ]

    # Find the best individual
    best = max(population, key=fitness)
    no_improve = 0

    # Repeat for given generations
    for generation in range(generations):

        new_population = []

        # Create new population
        while len(new_population) < pop_size:

            # Tournament selection
            def tournament_selection():
                candidates = random.sample(population, 3)
                return max(candidates, key=fitness)

            parent1 = tournament_selection()
            parent2 = tournament_selection()

            # Crossover
            if random.random() < crossover_rate:
                child = (parent1 + parent2) / 2
            else:
                child = parent1

            # Mutation
            if random.random() < mutation_rate:
                child += random.uniform(-1, 1)

            # Keep child within bounds
            child = max(x_min, min(x_max, child))

            new_population.append(child)

        # Update population
        population = new_population

        # Find fittest individual
        current_best = max(population, key=fitness)

        # Check improvement
        if fitness(current_best) > fitness(best):
            best = current_best
            no_improve = 0
        else:
            no_improve += 1

        print(
            f"Generation {generation + 1}: "
            f"Best x = {best:.4f}, "
            f"Fitness = {fitness(best):.4f}"
        )

        # Early stopping
        if no_improve >= patience:
            print("Stopping: No improvement!")
            break

    return best, fitness(best)


# Run Genetic Algorithm
best_x, best_fitness = genetic_algorithm()

print("\nFinal Result:")
print("Best x =", round(best_x, 4))
print("Maximum Fitness =", round(best_fitness, 4))
