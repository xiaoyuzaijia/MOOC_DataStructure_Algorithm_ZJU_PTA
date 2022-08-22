N, M = map(int, input().split())
E = {}
G1 = [[] for _ in range(N)]
G2 = [[] for _ in range(N)]
INDEGREE = [0 for _ in range(N)]
OUTDEGREE = [0 for _ in range(N)]

def TopSort1():
    earliest = [0 for _ in range(N)]
    q = []
    cnt = 0
    
    for i in range(N):
        if INDEGREE[i] == 0:
            q.append(i)
            cnt += 1
    
    while q:
        v = q.pop()
        for w in G1[v]:
            if earliest[v] + E[(v,w)] > earliest[w]:
                earliest[w] = earliest[v] + E[(v,w)]
            INDEGREE[w] -= 1
            if INDEGREE[w] == 0:
                q.append(w)
                cnt += 1
    
    if cnt < N:
        return False
    else:
        return earliest

def TopSort2(all_earliestTime):
    latest = [all_earliestTime for _ in range(N)]
    q = []
    
    for i in range(N):
        if OUTDEGREE[i] == 0:
            q.append(i)
    
    while q:
        w = q.pop()
        for v in G2[w]:
            if latest[w] - E[(v,w)] < latest[v]:
                latest[v] = latest[w] - E[(v,w)]
            OUTDEGREE[v] -= 1
            if OUTDEGREE[v] == 0:
                q.append(v)
    
    return latest


if __name__ == "__main__":
    for _ in range(M):
        a, b , weight = map(int, input().split())
        a -= 1
        b -= 1
        E[(a,b)] = weight
        G1[a].append(b)
        G2[b].append(a)
        INDEGREE[b] += 1
        OUTDEGREE[a] += 1
    
    earliest = TopSort1()
    if earliest:
        all_earliestTime = max(earliest)
        print(all_earliestTime)
    else:           # 不是DAG,直接退出程序  
        print(0)
        exit(0)
    latest = TopSort2(all_earliestTime)
    
    for v in range(N):
        for w in reversed(G1[v]):
            if latest[w] - earliest[v] - E[(v,w)] == 0:
                print(f"{v+1}->{w+1}")