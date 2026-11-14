import random

# Objective function
def f(x):
    return x**2

# Initialize parameters
N = 6              # Population size
G = 5              # Number of genes
Pc = 0.8           # Crossover probability
Pm = 0.1           # Mutation probability
MaxGen = 5       # Maximum generations

Xmin = 0
Xmax = 31

# Generate random population
P = [''.join(random.choice('01') for _ in range(G))
     for _ in range(N)]

# Decode binary chromosome into decimal
def decode(chromosome):
    D = int(chromosome, 2)
    x = Xmin + (D / (2**G - 1)) * (Xmax - Xmin)
    return x

# Calculate fitness
def fitness(chromosome):
    x = decode(chromosome)
    return 1 / (1 + f(x))

# Genetic Algorithm
for generation in range(MaxGen):

    # Fitness evaluation
    F = [fitness(ch) for ch in P]

    # Selection using roulette wheel
    new_population = []

    for i in range(N):
        selected = random.choices(P, weights=F, k=1)[0]
        new_population.append(selected)

    # Crossover
    offspring = []

    for i in range(0, N, 2):

        p1 = new_population[i]
        p2 = new_population[(i + 1) % N]

        if random.random() < Pc:
            k = random.randint(1, G - 1)

            c1 = p1[:k] + p2[k:]
            c2 = p2[:k] + p1[k:]

        else:
            c1 = p1
            c2 = p2

        offspring.extend([c1, c2])

    # Mutation
    mutated = []

    for chromosome in offspring[:N]:

        genes = list(chromosome)

        for j in range(G):
            if random.random() < Pm:
                genes[j] = '1' if genes[j] == '0' else '0'

        mutated.append(''.join(genes))

    # Population update
    combined = P + mutated

    combined.sort(key=fitness, reverse=True)

    P = combined[:N]

    # Best solution
    best = max(P, key=fitness)

    best_x = decode(best)

    print("Generation:", generation + 1,
          "Best Chromosome:", best,
          "X:", round(best_x, 4),
          "Fitness:", round(fitness(best), 6))

# Final output
best = max(P, key=fitness)

print("\nBest Solution:", decode(best))
print("Best Chromosome:", best)
print("Objective Function:", f(decode(best)))