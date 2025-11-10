from collections import deque

def water_jug(jug1,jub2,target):
    visited = set()
    q = deque()
    q.append((0,0,[]))

    while q:
        x,y,steps = q.popleft()
        if (x,y) in visited:
            continue
        visited.add((x,y))
        steps.append((x,y))

        if x == target or y == target:
            for idx, (a,b) in enumerate(steps):
                print(f"Step {idx}: Jug1 = {a}L, Jug2 = {b}L")
            print("done")
            return steps

        next_states = [
                ((jug1,y),"Fill Jug1"),


