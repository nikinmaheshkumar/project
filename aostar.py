def ao_star(graph, h, node):
    if node not in graph or not graph[node]:  # Goal/Terminal node
        return h[node], [node]
    min_cost = float('inf')
    min_path = []
    for cost, subnodes in graph[node]:
        total_cost = cost
        sub_paths = []
        for subnode in subnodes:
            sub_cost, sub_path = ao_star(graph, h, subnode)
            total_cost += sub_cost
            sub_paths.extend(sub_path)
        if total_cost < min_cost:
            min_cost = total_cost
            min_path = [node] + sub_paths
    return min_cost, min_path
graph_ao = {
    'A': [(2, ['B']), (4, ['C', 'D'])],
    'B': [],
    'C': [(2, ['E'])],
    'D': [],
    'E': [],
}
h_ao = {'A': 3, 'B': 0, 'C': 2, 'D': 0, 'E': 0}
cost, path = ao_star(graph_ao, h_ao, 'A')
print(f"AO* path: {path}, cost: {cost}")