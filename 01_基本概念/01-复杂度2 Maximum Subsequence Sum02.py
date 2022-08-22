k = int(input())
l = list(map(int, input().split()))
l.insert(0, 0)                # 0位置不使用
maxSum = -1
sum = [0 for _ in range(k+1)]
sum[0] = 0                    # 0位置不使用
for i in range(1, k+1):        # sum[i] 指从l[1]加到l[i]的和  
    sum[i] = sum[i-1] + l[i]
sta = 0
end = 1
for end in range(1, k+1):
    if (sum[end] - sum[sta]) > maxSum:
        maxSum = sum[end] - sum[sta]
        head = l[sta+1]
        rear = l[end]
    if sum[end] < sum[sta]:
        sta = end
if maxSum == -1:
    print('0' + ' ' + str(l[1]) + ' ' +str(l[k]))
else :
    print(str(maxSum) + ' ' + str(head) + ' ' + str(rear))