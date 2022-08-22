m, n, k = list(map(int, input().split()))
lines = []

for _ in range(k):
    lines.append(list(map(int, input().split())))
for line in lines:
    try:
        s = []
        pl = list(range(n, 0, -1))
        s.append(pl.pop())
        for i in line:
            while (s == []) or (s[-1] != i):
                s.append(pl.pop())
                if len(s) > m:
                    raise Exception("栈溢出")
            s.pop()
    except:
        print("NO")
    else:
        print("YES")