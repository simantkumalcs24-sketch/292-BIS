
import random

# Step 1: Input - Distance matrix between cities
distance = [
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 20],
    [20, 25, 30, 0, 15],
    [25, 30, 20, 15, 0]
]

# Parameters
num_ants = 5
iterations = 100
alpha = 1
beta = 2
rho = 0.5
Q = 100

n = len(distance)


# Ant Colony Optimization
def aco():

    # Step 2: Initialization
    pheromone = [[1.0 for j in range(n)] for i in range(n)]

    best_tour = []
    best_distance = float('inf')

    # Step 3: Repeat for each iteration
    for iteration in range(iterations):

        all_tours = []

        # For each ant
        for ant in range(num_ants):

            # Select random starting city
            start = random.randint(0, n - 1)

            visited = [start]
            current = start

            # While all cities are not visited
            while len(visited) < n:

                probabilities = []
                unvisited = []

                for city in range(n):

                    if city not in visited:

                        unvisited.append(city)

                        # Calculate probability
                        value = (
                            pheromone[current][city] ** alpha
                            * (1 / distance[current][city]) ** beta
                        )

                        probabilities.append(value)

                # Normalize probabilities
                total = sum(probabilities)

                probabilities = [
                    p / total for p in probabilities
                ]

                # Select next city based on probability
                next_city = random.choices(
                    unvisited,
                    weights=probabilities,
                    k=1
                )[0]

                visited.append(next_city)
                current = next_city

            # Return to starting city
            visited.append(start)

            # Calculate total tour distance
            tour_distance = sum(
                distance[visited[i]][visited[i + 1]]
                for i in range(n)
            )

            all_tours.append((visited, tour_distance))

            # Update best tour
            if tour_distance < best_distance:

                best_distance = tour_distance
                best_tour = visited.copy()

        # Step 4: Pheromone evaporation
        for i in range(n):
            for j in range(n):
                pheromone[i][j] *= (1 - rho)

        # Step 5: Pheromone deposit
        for tour, dist in all_tours:

            deposit = Q / dist

            for i in range(n):

                city1 = tour[i]
                city2 = tour[i + 1]

                pheromone[city1][city2] += deposit
                pheromone[city2][city1] += deposit

    # Step 6: Output
    return best_tour, best_distance


# Run ACO
best_tour, best_distance = aco()

print("Best Tour:", best_tour)
print("Shortest Distance:", best_distance)
