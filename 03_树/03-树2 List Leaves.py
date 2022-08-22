n = int(input())
nodel = []
check = [0 for _ in range(n)]
for i in range(n):
    node = tuple(map(int, input().replace('-', '-1').split()))
    node = (i, ) + node
    for j in node[1:]:
        if j >= 0:
            check[j] = 1
    nodel.append(node)

root = check.index(0)
q = [nodel[root]]
leaves = []

while q:
    current = q.pop(0)
    if current[1:] == (-1, -1):
        leaves.append(str(current[0]))
    else :
        if current[1] >= 0:
            q.append(nodel[current[1]])
        if current[2] >= 0:
            q.append(nodel[current[2]])

print(' '.join(leaves), end='')
