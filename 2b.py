import itertools

def tsp_brute_force(dist):
    n = len(dist)
    min_path = None
    min_cost = float('inf')
    for perm in itertools.permutations(range(1, n)):
        cost = dist[0][perm[0]]  # Start from city 0 to first city
        for i in range(len(perm)-1):
            cost += dist[perm[i]][perm[i+1]]  # Go through all cities in perm
        cost += dist[perm[-1]][0]  # Return to starting city
        if cost < min_cost:
            min_cost = cost
            min_path = (0,) + perm + (0,)
    return min_path, min_cost

dist_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

path, cost = tsp_brute_force(dist_matrix)
print(f"Optimal path: {path} with cost: {cost}")
