import copy

MAXDIST = 100000
N, M = map(int, input().split())


if __name__ == "__main__":
    G = [[MAXDIST for j in range(N)] for i in range(N)]
    for i in range(N):
        G[i][i] = 0
    for _ in range(M):
        i, j, weight = map(int, input().split())
        G[i-1][j-1] = weight
        G[j-1][i-1] = weight    # 反过来念咒语也可以,所以是无向图
    
    D = copy.deepcopy(G)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
    
    animal = 0
    maxcode = MAXDIST
    for i in range(N):
        if max(D[i]) < maxcode:
            animal = i
            maxcode = max(D[i])
    
    if maxcode == MAXDIST:
        print(animal)
    else:
        print(animal+1, maxcode)
