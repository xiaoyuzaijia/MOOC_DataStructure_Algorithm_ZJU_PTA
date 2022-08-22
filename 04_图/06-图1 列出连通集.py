def DFS(v):
    global N, Graph, L, Visited
    
    if Visited[v] is not None:
        L.append(v)
        Visited[v] = None
        for w in Graph[v]:
            DFS(w)

def BFS(v):
    global N, Graph, L, Visited, Q
    
    L.append(v)
    Visited[v] = None
    Q.append(v)
    while Q:
        v = Q.pop(0)
        for w in Graph[v]:
            if Visited[w] is not None:
                L.append(w)
                Visited[w] = None
                Q.append(w)

def listComponents(func):
    global N, L, Visited, RES
    
    for v in range(N):
        if Visited[v] is not None:
            func(v)
            RES.append("{ " + ' '.join(map(str, L)) + " }")
            L.clear()

N, E = map(int, input().split())
Graph = [[] for _ in range(N)]
Visited = [i for i in range(N)]
L = []
Q = []
RES = []

if __name__ == "__main__":
    for _ in range(E):
        a, b = map(int, input().split())
        Graph[a].append(b)
        Graph[b].append(a)
    for i in range(N):
        Graph[i].sort()
    
    listComponents(DFS)
    Visited = [i for i in range(N)]  # Visited初始化
    listComponents(BFS)
    print('\n'.join(RES), end='')