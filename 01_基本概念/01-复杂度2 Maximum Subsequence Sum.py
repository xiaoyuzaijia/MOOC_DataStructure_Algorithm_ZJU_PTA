k = int(input())
l = list(map(int, input().split()))
l.insert(0, 0)                   # 0位置不使用
sum = [0 for _ in range(k+1)]    # 0位置不使用 (一切问题都来源于此,不使用0位置后都解决了,令人感叹TAT)
maxSum = -1
head = 1
t_head = 1
rear = k
t_rear = k
for j in range(1, k+1):
    if sum[j-1] + l[j] >= l[j] :
        sum[j] = sum[j-1] + l[j]
        t_rear = j
    else :
        sum[j] = l[j]
        t_head = j
        t_rear = j
    if sum[j] > maxSum:
        maxSum = sum[j]
        head = t_head
        rear = t_rear
if maxSum == -1 :   # 如果为全负序列,maxSum不会更新,永远是-1
    maxSum = 0
    head = 1
    rear = k
print(str(maxSum) + ' ' + str(l[head]) + ' ' + str(l[rear]))
