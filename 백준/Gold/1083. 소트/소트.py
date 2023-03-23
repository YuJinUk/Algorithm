from sys import stdin
n=int(stdin.readline())
nums=list(map(int, stdin.readline().split()))
s=int(stdin.readline())
for i in range(n):
    if s==0:
        break
    max_num, idx = 0, 0
    for j in range(i, i+1+s):
        if j > n-1:
            break
        if max_num < nums[j]:
            max_num, idx = nums[j], j
    # print(max_num)
    # print(idx)
    s -= idx - i
    for j in range(idx, i, -1):
        nums[j]=nums[j-1]
    nums[i]=max_num
print(*nums)