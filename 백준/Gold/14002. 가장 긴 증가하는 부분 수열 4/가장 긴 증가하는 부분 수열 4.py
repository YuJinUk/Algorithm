from sys import stdin
n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
dp = [0] * n
for i in range(n):
    max_j = 0
    for j in range(i):
        if max_j <= dp[j] and nums[j] < nums[i]:
            dp[i] = dp[j]
            max_j = dp[j]
    dp[i] += 1
# print(dp)
m = max(dp)
print(m)
result = []
for i in range(len(dp)-1, -1, -1):
    if dp[i] == m:
        result.append(nums[i])
        m -= 1
result.reverse()
print(*result)