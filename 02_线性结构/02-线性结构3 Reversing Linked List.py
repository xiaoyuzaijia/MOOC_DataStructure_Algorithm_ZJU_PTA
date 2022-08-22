head, n, k = input().split()
n = int(n)
k = int(k)
d = {}
for _ in range(n):
    addr, data, next_ = input().split()
    d[addr] = (data, next_)
l = [(head, d[head][0])]   
for i in range(1, n):
    addri = d[l[i-1][0]][1]
    if addri == '-1':           # 是字符串的'-1',一开始没注意
        n = i
        break
    l.append((addri, d[addri][0]))

rl = []
rn = n//k   # 翻转的次数
if rn == 0:
    rl = l.copy()
else:
    for i in range(rn):
        sta = i * k   # 此次翻转的开始下标
        ex = l[sta:sta+k]
        ex.reverse()
        rl.extend(ex)
    rl.extend(l[sta+k:])   # 余下的全部extend过来
    rl.append(('-1', ''))  # 最后一个元素,方便输出

for i in range(n):
    print(rl[i][0], rl[i][1], rl[i+1][0])
