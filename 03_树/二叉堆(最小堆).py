class BinHeap :
    def __init__(self) :
        self.heapList = [0]
        self.size = 0

    def precUp(self,i) :   #将i位置的值上浮
        while i//2 > 0 :
            if self.heapList[i] < self.heapList[i//2] :  #小于父节点就交换
                self.heapList[i] , self.heapList[i//2] = self.heapList[i//2] , self.heapList[i]
            else :
                break
            i = i//2

    def insert(self,val) :
        self.heapList.append(val)   #新值插入到末尾
        self.size += 1
        self.precUp(self.size)      #新值上浮

    def minChild(self,i) :   #返回i位置的最小子节点的位置
        if i*2+1 > self.size :   #唯一子节点
            return i*2
        else :
            if self.heapList[i*2] < self.heapList[i*2+1] :   #左子节点更小
                return i*2
            else :                                           #右子节点更小
                return i*2+1

    def precDown(self,i) :   #将i位置值的下沉
        while i*2 <= self.size :
            mc = self.minChild(i)
            if self.heapList[mc] < self.heapList[i] :   #最小子节点比自己小,可以下沉
                self.heapList[mc] , self.heapList[i] = self.heapList[i] , self.heapList[mc]
            else :
                break
            i = mc

    def delMin(self) :    #删除堆顶并返回堆顶值
        min = self.heapList[1]
        self.heapList[1] , self.heapList[self.size] = self.heapList[self.size] , self.heapList[1]
        self.heapList.pop()
        self.size -= 1
        self.precDown(1)   #新顶下沉
        return min

    def buildHeap(self,alist:list) :   #从无序表生成二叉堆,并返回这个堆
        self.heapList = [0] + alist.copy()
        self.size = len(self.heapList) - 1
        i = self.size // 2    #从最后一个节点的父节点开始,因为叶节点无需下沉
        while i > 0 :             
            self.precDown(i)      #从后往前依次下沉
            i -= 1
        return self.heapList

binHeap = BinHeap()
binHeap.buildHeap([97,76,65,50,49,13,27])
print(binHeap.heapList)
binHeap.insert(83)
print(binHeap.heapList)