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

def get_max_child(heap_l, heap_size, i):
    if i*2+1 > heap_size:
        return i*2
    else:
        return max(i*2, i*2+1, key=lambda x: heap_l[x])

def prec_down(heap_l, heap_size, i):
    while i*2 <= heap_size:
        max_child = get_max_child(heap_l, heap_size, i)
        if heap_l[i] < heap_l[max_child]:
            heap_l[i], heap_l[max_child] = heap_l[max_child], heap_l[i]
        else:
            break
        i = max_child

def heap_sort(l):
    flag = 0
    heap_size = len(l)
    l.insert(0, None)  # 0位置不使用

    for i in range(heap_size//2, 0, -1):
        prec_down(l, heap_size, i)
    for _ in range(N-1):
        l[1], l[heap_size] = l[heap_size], l[1]  # 从最大堆中拿一个放末尾
        heap_size -= 1                               # 堆中元素数量减一
        prec_down(l, heap_size, 1)
        if l[1:] == partsort_l:
            flag = 1
            continue
        if flag == 1:
            return l[1:]
    return False



if __name__ == "__main__":
    next_part_sort_l = insertion_sort(unsort_l.copy())
    if next_part_sort_l:
        print("Insertion Sort")
        print(' '.join(map(str, next_part_sort_l)))
    else:
        print("Heap Sort")
        next_part_sort_l = heap_sort(unsort_l.copy())
        print(' '.join(map(str, next_part_sort_l)))
