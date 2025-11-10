from queue import PriorityQueue
def astar(graph, start, goal, h):
    pq=PriorityQueue() 
    pq.put((h[start],0,start,[start]))
    seen=set()
    while not pq.empty():
        f,g,node,path = pq.get()
        if node==goal: return path,g
        if node in seen: continue
        seen.add(node)
        for nei,cost in graph[node].items():
            if nei not in seen: pq.put((g+cost+h[nei], g+cost, nei, path+[nei]))
    return None, float('inf')
def main():
    graph = {'A':{'B':1,'C':4}, 'B':{'C':2,'D':5}, 'C':{'D':1}, 'D':{}}
    h = {'A':3,'B':2,'C':1,'D':0}
    path, cost = astar(graph,'A','D',h)
    print('Path:', path, 'Cost:', cost)
if __name__ == '__main__':
    main()