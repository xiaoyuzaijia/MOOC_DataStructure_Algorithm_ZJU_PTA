s = input()
N = int(input())


def get_match(p):
    match = [0 for _ in range(len(p))]
    
    for j in range(1, len(p)):
        i = match[j-1]
        while i >= 1 and p[i] != p[j]:
            i = match[i-1]
        if p[i] == p[j]:
            match[j] = i + 1
        else:
            match[j] = 0

    return match

def KMP(s, p):
    match = get_match(p)
    
    i = 0
    j = 0
    while i < len(s) and j < len(p):
        if s[i] == p[j]:
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            j = match[j-1]
    if j == len(p):
        return i - j
    else:
        return -1

if __name__ == "__main__":
    for _ in range(N):
        p = input()
        found = KMP(s, p)
        if found != -1:
            print(s[found:])
        else:
            print("Not Found")


"""
pypy3最后一个测试点超时
"""
