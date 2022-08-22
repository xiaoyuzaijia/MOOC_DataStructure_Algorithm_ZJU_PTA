def isSame(x:list, y:list) -> bool:
    if (not x) and (not y):  # 都是空列表
        return True
    elif (len(x) != len(y)) or (x[0] != y[0]):   # 长度不等 或 根不同
        return False
    else:
        xl = list(filter(lambda z: z < x[0], x))
        xr = list(filter(lambda z: z > x[0], x))
        yl = list(filter(lambda z: z < y[0], y))
        yr = list(filter(lambda z: z > y[0], y))
        if isSame(xl, yl) and isSame(xr, yr):    # x的左子树和y的左子树是同一棵 并且 x的右子树和y的右子树是同一棵
            return True
        else :
            return False

resultl = []
putin = list(map(int, input().split()))
while (putin[0] != 0):
    x = list(map(int, input().split()))
    for _ in range(putin[1]):
        y = list(map(int, input().split()))
        if isSame(x, y):
            resultl.append("Yes")
        else:
            resultl.append("No")
    putin = list(map(int, input().split()))
print('\n'.join(resultl), end='')