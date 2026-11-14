
import random

# Fitness function
def fitness(x):
    return -x**2 + 10*x + 5


# PSO Algorithm
def pso():

    # Parameters
    pop_size = 10
    max_iterations = 100
    c1 = 1
    c2 = 1

    # Step 1: Particle initialization
    P = [random.uniform(0, 10) for _ in range(pop_size)]

    # Initialize personal best
    pbest = P.copy()

    # Initialize velocity
    V = [0.0] * pop_size

    # Step 2: Repeat for maximum iterations
    for I in range(max_iterations):

        # For each particle
        for i in range(pop_size):

            # Calculate fitness
            fp = fitness(P[i])

            # Update personal best
            if fp > fitness(pbest[i]):
                pbest[i] = P[i]

        # Step 3: Find global best
        gbest = max(pbest, key=fitness)

        # Step 4: Update velocity and position
        for i in range(pop_size):

            U1 = random.random()
            U2 = random.random()

            # Update velocity
            V[i] = (V[i]
                    + c1 * U1 * (pbest[i] - P[i])
                    + c2 * U2 * (gbest - P[i]))

            # Update position
            P[i] = P[i] + V[i]

    # Step 6: Return global best
    return gbest


# Run PSO
result = pso()

print("Best X =", round(result, 4))
print("Maximum Fitness =", round(fitness(result), 4))
