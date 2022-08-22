class UnionFind(object):
    def __init__(self, n):   # n是总节点数量
        self.uf = [-1 for _ in range(n+1)]  # 下标代表节点,列表元素代表父节点
        self.sets_count = n   #当前的集合数量,初始认为有n个

    def findRoot(self, x):
        r = x
        while self.uf[r] > 0:
            r = self.uf[r]
        while x != r:   # 此时r是x的根,路径压缩,把搜索下来的结点的父全指向根
            p = self.uf[x]
            self.uf[x] = r
            x = p
        return r

    def union(self, x, y):
        xroot = self.findRoot(x)
        yroot = self.findRoot(y)
        if xroot == yroot:   # x, y在同一个集合,无需连通
            return
        elif self.uf[xroot] < self.uf[yroot]: # 负数越小规模越大
            self.uf[xroot] += self.uf[yroot]  # 规模小的加到规模大的根下
            self.uf[yroot] = xroot
        else:
            self.uf[yroot] += self.uf[xroot]
            self.uf[xroot] = yroot
        self.sets_count -= 1  # 连通后总集合数-1

    def isConnect(self, x, y):
        return self.findRoot(x) == self.findRoot(y)

N = int(input())
myUF = UnionFind(N)
while True:
    op = input().split()
    if op[0] == 'C':
        if myUF.isConnect(int(op[1]), int(op[2])):
            print("yes")
        else:
            print("no")
    elif op[0] == 'I':
        myUF.union(int(op[1]), int(op[2]))
    elif op[0] == 'S':
        break
if myUF.sets_count == 1:
    print("The network is connected.")
else:
    print(f"There are {myUF.sets_count} components.")