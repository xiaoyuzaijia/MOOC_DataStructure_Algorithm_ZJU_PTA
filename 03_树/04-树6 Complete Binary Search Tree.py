def inOrderTraver(i):
    global n, t, inOrderL
    if i <= n:
        inOrderTraver(2 * i)
        t[i] = inOrderL.pop()
        inOrderTraver(2 * i +1)

n = int(input())
t = [-1 for _ in range(n+1)]
inOrderL = list(map(int, input().split()))
inOrderL.sort(reverse=True)
inOrderTraver(1)
t.pop(0)
print(' '.join(map(str, t)))