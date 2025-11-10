from collections import deque
MOVES = ((1,0),(2,0),(0,1),(0,2),(1,1))
def valid(s):
    m1,c1,m2,c2,_ = s
    return min(m1,c1,m2,c2) >= 0 and (m1==0 or m1>=c1) and (m2==0 or m2>=c2)
def successors(s):
    m1,c1,m2,c2,b = s
    res = []
    for m,c in MOVES:
        ns = (m1-m,c1-c,m2+m,c2+c,0) if b else (m1+m,c1+c,m2-m,c2-c,1)
        if valid(ns): res.append(ns)
    return res
def bfs():
    start = (3,3,0,0,1)
    goal = (0,0,3,3,0)
    q = deque([(start,[start])])
    seen = {start}
    while q:
        s,path = q.popleft()
        if s[:4] == goal[:4]: return path
        for ns in successors(s):
            if ns not in seen: 
                seen.add(ns) 
                q.append((ns,path+[ns]))
def main():
    sol = bfs()
    for a,b,c,d,e in sol:
        print(f"L:{a}M,{b}C | R:{c}M,{d}C | Boat:{'L' if e else 'R'}")
if __name__ == '__main__':
    main()