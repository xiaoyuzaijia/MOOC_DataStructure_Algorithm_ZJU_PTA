MAXDIST = 100000
N, M, S, D = map(int, input().split())
G = [[] for _ in range(N)]
Weight = [[MAXDIST for _ in range(N)] for _ in range(N)]
Cost = [[MAXDIST for _ in range(N)] for _ in range(N)]
for i in range(N):
    Weight[i][i] = 0
    Cost[i][i] = 0

def findMin(visited, dist):
    minDist = MAXDIST
    minV = -1
    for v in range(N):
        if (not visited[v]):
            if dist[v] < minDist:
                minDist = dist[v]
                minV = v
    return minV

def dijkstra(s:int, edge:list):
    visited = [False for _ in range(N)]
    visited[s] = True
    dist = [MAXDIST for _ in range(N)]
    cost = [MAXDIST for _ in range(N)]
    dist[s] = 0
    cost[s] = 0
    for w in G[s]:
        dist[w] = edge[s][w]
        cost[w] = Cost[s][w]
    
    while True:
        v = findMin(visited, dist, cost)
        if v == -1:
            break
        visited[v] = True
        for w in G[v]:
            if (not visited[w]):
                if dist[v] + edge[v][w] < dist[w]:
                    dist[w] = dist[v] + edge[v][w]
                    cost[w] = cost[v] + Cost[v][w]
                elif dist[v] + edge[v][w] == dist[w]:  # 长度相同的话,如果花费更小就更新
                    if cost[v] + Cost[v][w] < cost[w]:
                        dist[w] = dist[v] + edge[v][w]
                        cost[w] = cost[v] + Cost[v][w]
    
    return dist[D], cost[D]



if __name__ == "__main__":
    for _ in range(M):
        a, b, weight, cost = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
        Weight[a][b] = Weight[b][a] = weight
        Cost[a][b] = Cost[b][a] = cost
    minWeight, allCost = dijkstra(S, Weight)
    print(minWeight, allCost)


# 用python3超时,用pypy3不超时(251ms)