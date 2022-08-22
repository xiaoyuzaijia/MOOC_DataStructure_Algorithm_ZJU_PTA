N = int(input())
unsort_l = list(map(int, input().split()))
partsort_l = list(map(int, input().split()))

def insertion_sort(l):
    flag = 0
    
    for p in range(1, N):
        tmp = l[p]
        i = p
        while i > 0 and l[i-1] > tmp:
            l[i] = l[i-1]
            i -= 1
        l[i] = tmp
        if l == partsort_l:
            flag = 1
            continue
        if flag == 1:
            return l
    return False

def merge(l1, l2):
    merge_l = []
    
    while l1 and l2:
        merge_l.append(l1.pop(0) if l1[0]<l2[0] else l2.pop(0))
    merge_l.extend(l1 if l1 else l2)
    
    return merge_l

def merge_sort(l):
    flag = 0
    
    d = 1
    while d < N:
        d *= 2
        tmp_l = []
        for i in range(0, N, d):
            tmp_l.extend(merge(l[i:i+d//2], l[i+d//2:i+d]))
        l = tmp_l
        if l == partsort_l:
            flag = 1
            continue
        if flag == 1:
            return l
    return False


if __name__ == "__main__":
    next_part_sort_l = insertion_sort(unsort_l.copy())
    if next_part_sort_l:
        print("Insertion Sort")
        print(' '.join(map(str, next_part_sort_l)))
    else:
        print("Merge Sort")
        next_part_sort_l = merge_sort(unsort_l.copy())
        print(' '.join(map(str, next_part_sort_l)))
