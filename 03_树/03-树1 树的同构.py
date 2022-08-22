def buildTree():
    n = int(input())
    datal = []
    leftl = []
    rightl = []
    check = [0 for _ in range(n)]
    for _ in range(n):
        data, left, right = input().split()
        datal.append(data)
        if left != '-':
            left = int(left)
            check[left] = 1
            leftl.append(left)
        else:
            leftl.append('-')
        if right != '-':
            right = int(right)
            check[right] = 1
            rightl.append(right)
        else:
            rightl.append('-')
    if n:
        root = datal[check.index(0)]
    else:
        root = '-'
    t = {}
    for i in range(n):
        left = datal[leftl[i]] if leftl[i] != '-' else '-'
        right = datal[rightl[i]] if rightl[i] != '-' else '-'
        t[datal[i]] = (left, right)
    return (t.copy(), root, n)

t1, r1, n1= buildTree()
t2, r2, n2 = buildTree()
try:
    if n1 == 0 and n2 == 0:
        pass
    else:
        if n1 != n2:
            raise Exception("node nums is not equal")
        elif r1 != r2:
            raise Exception("root is not same")
        else:
            for data in t1.keys():
                if (t1[data] == t2[data]) or (t1[data] == t2[data][::-1]):
                    pass
                else:
                    raise Exception("this node is not isom")
except:
    print("No", end='')
else:
    print("Yes", end='')
