# This program solves trivial traveling salesman problems. 
# It's useful for planning vacations that involve a lot of driving.
# I initially created this when I visited Anaheim California in March 2025

import numpy as np
from python_tsp.heuristics import solve_tsp_simulated_annealing

# Define a distance matrix
# for typical usage, go through google maps and find the time it takes to go from one place to the next, and do every permutation
# the diagonal being the zero identity is a result that the i-th column is equal to the i-th row
distance_matrix = np.array([
[0,    1.5, 1.2, 1,   0.5],
[1.5, 0,   0.3, 1,   0.75],
[1.2, 0.3, 0,   0.8, 0.75],
[1,   1,   0.8, 0,   0.5],
[0.5,    0.75,    0.75,    0.5, 0]
])

# Example: where the numbers are the time in minutes it takes to get from place to place

#          Place 1:  Place 2: Place 3
#Place 1:     0         40      60
#Place 2:    40          0      75
#Place 3:    60         75       0


# Solve the TSP using simulated annealing
permutation, distance = solve_tsp_simulated_annealing(distance_matrix)

# Print the results
print("Optimal permutation (route):", permutation)
print("Total distance:", distance)
