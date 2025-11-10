from collections import deque

def valid(state):
    m1, c1, m2, c2, boat = state
    if m1 < 0 or m2 < 0 or c1 < 0 or c2 < 0:
        return False
    if (m1 > 0 and m1 < c1) or (m2 > 0 and m2 < c2):
        return False
    return True

def successors(state):
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    results = []
    for m, c in moves:
        m1, c1, m2, c2, boat = state
        if boat == 1: # Left to Right
            new_state = (m1-m, c1-c, m2+m, c2+c, 0)
        else: # Right to Left
            new_state = (m1+m, c1+c, m2-m, c2-c, 1)
        if valid(new_state):
            results.append(new_state)
    return results

def bfs():
    start = (3,3,0,0,1)
    goal = (0,0,3,3,0)
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state[:4] == goal[:4]:
            return path
        visited.add(state)
        for succ in successors(state):
            if succ not in visited:
                queue.append((succ, path + [succ]))
    return None

solution = bfs()
steps = [f"Left: {s[0]}M, {s[1]}C | Right: {s[2]}M, {s[3]}C | Boat: {'Left' if s[4]==1 else 'Right'}" for s in solution]
print('\n'.join(steps))