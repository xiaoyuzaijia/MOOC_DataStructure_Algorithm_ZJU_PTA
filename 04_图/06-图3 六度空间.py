N, M = map(int, input().split())
G = [[] for _ in range(N+1)]


def BFS(sta):
    visited = [False for _ in range(N+1)]
    q = []
    q.append(sta)
    visited[sta] = True
    count = 1
    level = 0
    last = sta
    while q:
        v = q.pop(0)
        for w in G[v]:
            if not visited[w]:
                visited[w] = True
                q.append(w)
                count += 1
                tail = w
        if v == last:
            level += 1
            last = tail
        if level == 6:
            break
    return count



def listConponents():
    for v in range(1, N+1):
        count = BFS(v)
        print(f"{v}: {count/N:.2%}")


if __name__ == "__main__":
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    listConponents()