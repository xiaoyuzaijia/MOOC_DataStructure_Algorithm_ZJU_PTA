class MinBinHeap:
    def __init__(self):
        self.heapList = [None]
        self.size = 0

    def insert(self, data):
        self.heapList.append(data)
        self.size += 1
        self.precUp(self.size)

    def precUp(self, i):
        while i//2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                self.heapList[i], self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
            else:
                break
            i = i//2

    def getPath(self, i) ->list :     # 从下标i的节点,到根节点路径上的数据
        pathl = []
        while i > 0:
            pathl.append(self.heapList[i])
            i = i//2
        return pathl

n, m = map(int, input().split())
myHeap = MinBinHeap()
for i in map(int, input().split()):
    myHeap.insert(i)
for i in map(int, input().split()):
    print(' '.join(map(str, myHeap.getPath(i))), end='')
    m -= 1
    if m:
        print()