N, M = map(int, input().split())
G = [[] for _ in range(N)]
E = {}
INDEGREE = [0 for _ in range(N)]

def TopSort():
    earliest = [0 for _ in range(N)]
    q = []
    cnt = 0
    
    for i in range(N):
        if INDEGREE[i] == 0:
            q.append(i)
            cnt += 1
    
    while q:
        v = q.pop()
        for w in G[v]:
            if earliest[v] + E[(v,w)] > earliest[w]:
                earliest[w] = earliest[v] + E[(v,w)]
            INDEGREE[w] -= 1
            if INDEGREE[w] == 0:
                q.append(w)
                cnt += 1
    
    if cnt < N:
        return False
    else:
        return max(earliest)

if __name__ == "__main__":
    for _ in range(M):
        a, b , weight = map(int, input().split())
        G[a].append(b)
        E[(a,b)] = weight
        INDEGREE[b] += 1
    earliestTime = TopSort()
    if earliestTime:
        print(earliestTime)
    else:
        print("Impossible")
    