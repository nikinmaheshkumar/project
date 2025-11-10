from collections import deque
def water_jug_bfs(j1, j2, target):
    q = deque([((0,0),[])])
    seen = set()
    while q:
        (x,y), path = q.popleft()
        if (x,y) in seen: continue
        seen.add((x,y))
        path = path+[(x,y)]
        if x==target or y==target:
            return path
        nxt = [
            (j1,y), (x,j2), (0,y), (x,0),
            (min(j1,x+y), max(0,x+y-j1)),
            (max(0,x+y-j2), min(j2,x+y))
        ]
        for s in nxt:
            if s not in seen: q.append((s, path))
    return None
def main():
    path = water_jug_bfs(4, 3, 2)
    print("Path:", path)

if __name__ == '__main__':
    main()