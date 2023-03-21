from sys import stdin
n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
dp = [0] * n
for i in range(n):
    min_j = 0
    for j in range(i):
        if min_j < dp[j] and nums[j] > nums[i]:
            dp[i] = dp[j]
            min_j = dp[j]
    dp[i] += 1
# print(dp)
print(max(dp))