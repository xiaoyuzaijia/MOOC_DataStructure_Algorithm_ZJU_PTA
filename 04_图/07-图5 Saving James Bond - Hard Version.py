from math import pow

N, D = map(int, input().split())
G = []
Dist = {}
Path = {}
Q = []

def canJump(a, b):
    return pow(D, 2) >= pow(a[0]-b[0], 2) +pow(a[1]-b[1], 2)

def firstJump(a):
    return pow(D+7.5, 2) >= pow(a[0]-0, 2) +pow(a[1]-0, 2) > pow(+7.5, 2)  # 在岛上的顶点不能作为起点

def outJump(a):
    return a[0]+D >= 50 or a[1]+D >= 50 or a[0]-D<=-50 or a[1]-D<=-50

def distOfTwo(a, b):
    return pow(a[0]-b[0], 2) +pow(a[1]-b[1], 2)

def dijkstra(s):
    minJumps = 10000
    outV = (0,0)

    Q.append(s)
    Dist[s] = 0
    while Q:
        v = Q.pop(0)
        if outJump(v) and Dist[v] < minJumps:
            minJumps = Dist[v]
            outV = v
        for w in G:
            if Dist[w] == -1 and canJump(v, w):
                Dist[w] = Dist[v] + 1
                Path[w] = v
                Q.append(w)
    else:
        return minJumps, Path.copy(), outV

def getPath(v):
    if allminPath[v] == -1:
        print(v[0], v[1])
        return
    getPath(allminPath[v])
    print(v[0], v[1])


for _ in range(N):
    v = tuple(map(int, input().split()))
    G.append(v)
    Dist[v] = -1
    Path[v] = -1

firstVerL = list(filter(lambda x: firstJump(x), G))
firstVerL.sort(key=lambda x: distOfTwo(x, (0,0)))
allminJumps = 10000
allminPath = {}
alloutV = (0,0)
for s in firstVerL:
    minJumps, minPath, outV = dijkstra(s)
    if minJumps < allminJumps:
        allminJumps = minJumps
        allminPath = minPath
        alloutV = outV
    for _ in range(N):
        Dist[v] = -1
        Path[v] = -1

if D+7.5 >= 50:   # 能一步跳出直接输出1,不用输出路径
    print(1) 
elif allminJumps == 10000:
    print(0)
else:
    print(allminJumps+2)  # 加上第一跳和最后一跳
    getPath(alloutV)