import heapq

class UnionFind(object):
    def __init__(self, n):
        self.uf = [-1 for _ in range(n+1)]
        self.sets_count = n
    
    def findRoot(self, x):
        r = x
        while self.uf[r] > 0:
            r = self.uf[r]
        while self.uf[x] > 0:
            p = self.uf[x]
            self.uf[x] = r
            x = p
        return r
    
    def union(self, x, y):
        xroot = self.findRoot(x)
        yroot = self.findRoot(y)
        if xroot == yroot:
            return
        elif self.uf[xroot] < self.uf[yroot]:
            self.uf[xroot] += self.uf[yroot]
            self.uf[yroot] = xroot
        else:
            self.uf[yroot] += self.uf[xroot]
            self.uf[xroot] = yroot
        self.sets_count -= 1
    
    def isConnect(self, x, y):
        return self.findRoot(x) == self.findRoot(y)

def Kruskal():
    mst = []
    while E and len(mst) < N-1:
        e = heapq.heappop(E)
        if not MYUF.isConnect(e[1], e[2]):
            mst.append(e)
            MYUF.union(e[1], e[2])
    if len(mst) < N-1:
        return False
    else:
        return mst

N, M = map(int, input().split())
E = []
MYUF = UnionFind(N)
if __name__ == "__main__":
    for _ in range(M):
        heapq.heappush(E, tuple(map(int, reversed(input().split()))))
    mst = Kruskal()
    if mst:
        print(sum(i[0] for i in mst))
    else:
        print(-1)
