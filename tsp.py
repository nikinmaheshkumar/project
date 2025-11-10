import itertools
def tsp_brute_force(dist):
    n = len(dist); best=(None,float('inf'))
    for perm in itertools.permutations(range(1,n)):
        cost = dist[0][perm[0]] + sum(dist[perm[i]][perm[i+1]] for i in range(len(perm)-1)) + dist[perm[-1]][0]
        if cost < best[1]: best=( (0,)+perm+(0,), cost)
    return best
def main():
    dist = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    path, cost = tsp_brute_force(dist)
    print('Best path:', path)
    print('Cost:', cost)
if __name__ == '__main__':
    main()