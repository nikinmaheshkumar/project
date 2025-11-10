from queue import PriorityQueue

def astar(graph, start, goal, h):
    pq = PriorityQueue()
    pq.put((h[start], 0, start, [start]))
    visited = set()
    while not pq.empty():
        est_total, cost, curr, path = pq.get()
        if curr == goal:
            return path, cost
        if curr in visited:
            continue
        visited.add(curr)
        for neighbor, edge_cost in graph[curr].items():
            if neighbor not in visited:
                pq.put((cost + edge_cost + h[neighbor], cost + edge_cost, neighbor, path + [neighbor]))
    return None, float('inf')

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 1, 'E': 5},
    'C': {'F': 2},
    'D': {'G': 2},
    'E': {'G': 2},
    'F': {'G': 2},
    'G': {}
}
h = {'A': 4, 'B': 2, 'C': 2, 'D': 3, 'E': 1, 'F': 2, 'G': 0}

astar_path, astar_cost = astar(graph, 'A', 'G', h)
print(f"A* path: {astar_path}, cost: {astar_cost}")