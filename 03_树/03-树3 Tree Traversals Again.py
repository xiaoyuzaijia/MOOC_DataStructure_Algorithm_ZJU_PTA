n = int(input())
prel = []
s = []
inl = []
for _ in range(2*n):
    op = input().split()
    if op[0] == "Push":
        prel.append(int(op[1]))
        s.append(int(op[1]))
    else:
        inl.append(s.pop())

def getPostl(prel:list, inl:list) -> list:  # 根据前序和后序通过递归获得后序
    if len(prel) <= 1:
        return prel
    else:
        root = prel[0]
        rootIdx = inl.index(root)
        leftPostl = getPostl(prel[1:rootIdx+1], inl[:rootIdx])
        rightPostl = getPostl(prel[rootIdx+1:], inl[rootIdx+1:])
        postl = leftPostl
        postl.extend(rightPostl)
        postl.append(root)
        return postl

postl = getPostl(prel, inl)
postl = list(map(str, postl))
print(' '.join(postl), end='')
