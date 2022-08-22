n = int(input())
l = map(int, input().split())
print(' '.join(map(str, sorted(l))), end='')