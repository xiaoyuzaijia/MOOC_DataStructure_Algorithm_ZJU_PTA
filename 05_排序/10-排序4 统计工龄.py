N = int(input())

if __name__ == "__main__":
    l = [0 for _ in range(51)]
    inl = map(int, input().split())
    for i in inl:
        l[i] += 1
    for i in range(51):
        if l[i] != 0:
            print(f"{i}:{l[i]}")