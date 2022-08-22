def check():
    global N, F, WPL
    wpl = 0
    col = []
    for _ in range(N):
        ch, co = input().split()
        col.append(co)
        wpl += F[ch] * len(co)
    if wpl != WPL:
        return False
    for i in col:   # 判断前缀
        colCmp = list(filter(lambda s: len(s)>=len(i), col))   # 只与比自己长度大于等于的编码比
        colCmp.remove(i)   # 移除自己
        for j in colCmp:
            try:
                if j.index(i) == 0:
                    return False
            except:
                pass
    return True


N = int(input())
l = input().split()
M =int(input())
F = {}
for i in range(0, 2*N, 2):
    F[l[i]] = int(l[i+1])
q = list(F.values())
WPL = 0
for _ in range(N-1):
    q.sort(reverse=True)
    new = q.pop() + q.pop()
    WPL += new
    q.append(new)
for _ in range(M):
    if check():
        print("Yes")
    else:
        print("No")



'''
3 最大N&M，code长度等于63 运行超时 0 -- 2884 KB
'''