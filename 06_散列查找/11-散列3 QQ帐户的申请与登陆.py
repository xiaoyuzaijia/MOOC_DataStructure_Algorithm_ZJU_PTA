N = int(input())
d = {}

if __name__ == "__main__":
    for _ in range(N):
        op, qqid, password = input().split()
        qqid = int(qqid)
        
        if op == "N":
            if qqid not in d:
                d[qqid] = password
                print("New: OK")
            else:
                print("ERROR: Exist")
        elif op == "L":
            if qqid in d:
                if password == d[qqid]:
                    print("Login: OK")
                else:
                    print("ERROR: Wrong PW")
            else:
                print("ERROR: Not Exist")
                