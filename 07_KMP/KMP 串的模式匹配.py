s = input()
N = int(input())

if __name__ == "__main__":
    for _ in range(N):
        p = input()
        found = s.find(p)
        if found != -1:
            print(s[found:])
        else:
            print("Not Found")
