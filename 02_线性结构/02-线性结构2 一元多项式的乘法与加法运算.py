l1 = list(map(int, input().split()[1:]))
l2 = list(map(int, input().split()[1:]))
p1 = list(zip(l1[::2], l1[1::2]))
p2 = list(zip(l2[::2], l2[1::2]))

def add(p1:list, p2:list) ->list :
    ps = []
    while p1 and p2:
        if p1[0][1] > p2[0][1]:
            ps.append(p1.pop(0))
        elif p1[0][1] < p2[0][1]:
            ps.append(p2.pop(0))
        else :                  # 合并
            e = p1[0][1]                     # 指数
            c = p1.pop(0)[0] + p2.pop(0)[0]  # 系数
            if c != 0:                       # 合并后系数为零的抵消掉
                ps.append((c, e))
    if p1 :
        if p1 != [(0,0)]:                    # 仅仅是为了处理p1为[(0,0)]的情况,下同
            ps.extend(p1)
    else :
        if p2 != [(0,0)]:
            ps.extend(p2)
    return ps

def mul(p1:list, p2:list) -> list :
    pp = []
    for c1, e1 in p1:
        for c2, e2 in p2:
            if c1*c2 != 0:                  # 系数为零这一项就不加了
                pp = add(pp.copy(), [(c1*c2, e1+e2)])
    return pp

pp = mul(p1.copy(), p2.copy())
ps = add(p1.copy(), p2.copy())
pp2 = []
ps2 = []
for ce in pp:
    pp2.extend(list(map(str, ce)))
for ce in ps:
    ps2.extend(list(map(str, ce)))
if not pp2 :
    pp2 = ['0', '0']
if not ps2 :
    ps2 = ['0', '0']
print(' '.join(pp2))
print(' '.join(ps2))