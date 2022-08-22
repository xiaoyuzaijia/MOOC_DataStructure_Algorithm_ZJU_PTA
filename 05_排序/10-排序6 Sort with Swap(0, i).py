N = int(input())
l = list(map(int, input().split()))

if __name__ == "__main__":
    this_circle_element_num = 0
    i = 0
    while l[i] != i:
        next = l[i]
        l[i] = i
        i = next
        this_circle_element_num += 1
    swaps = this_circle_element_num - 1 if this_circle_element_num > 0 else 0


    for i in range(N):
        if l[i] == i:
            continue
        this_circle_element_num = 0
        while l[i] != i:
            next = l[i]
            l[i] = i
            i = next
            this_circle_element_num += 1
        swaps += this_circle_element_num + 1
        
    print(swaps)