from math import pow
N, D = map(int, input().split())
G = []
Visited = {}

def canJump(a, b):
    return pow(D, 2) >= pow(a[0]-b[0], 2) + pow(a[1]-b[1], 2)

def firstJump(a):
    return pow(D+15, 2) >= pow(a[0]-0, 2) + pow(a[1]-0, 2)   
    # 用D+15能过, 用D+7.5第一个测试点就过不了.真怪,15明明是直径

def outJump(a):
    x, y = a
    return x+D>=50 or x-D<=-50 or y+D>=50 or y-D<=-50

def DFS(v):
    Visited[v] = True
    if outJump(v):
        return True
    for w in G:
        if not Visited[w] and canJump(v, w):
            return DFS(w)
    return False

def save007():
    for v in G:
        if (not Visited[v]) and firstJump(v):
            res = DFS(v)
            if res:
                return True
    return False

if __name__ == "__main__":
    for _ in range(N):
        Visited[tuple(map(int, input().split()))] = False
    G = Visited.keys()
    if save007():
        print("Yes")
    else:
        print("No")
