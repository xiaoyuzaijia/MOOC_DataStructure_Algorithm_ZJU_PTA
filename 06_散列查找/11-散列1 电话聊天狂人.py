N = int(input())
d = {}

if __name__ == "__main__":
    for _ in range(N):
        x, y = map(int, input().split())
        if x not in d:
            d[x] = 0
        if y not in d:
            d[y] = 0
        d[x] += 1
        d[y] += 1
    
    max_tele = max(d.keys(), key=lambda x: (d[x], -x))
    max_tele_num = list(d.values()).count(d[max_tele])
    if max_tele_num == 1:
        print(max_tele, d[max_tele])
    else:
        print(max_tele, d[max_tele], max_tele_num)