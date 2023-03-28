n = int(input())
nums = list(map(int, input().split()))
# dp = [[float('-inf')] * n for _ in range(n)]
# for i in range(n):
#     dp[i][i] = nums[i]
# for i in range(n-1):
#     for j in range(i+1, n):
#         dp[i][j] = dp[i][j-1] + nums[j]
# print(max(map(max, dp)))
dp = [nums[0]]
for i in range(1, n):
    dp.append(max(dp[i-1] + nums[i], nums[i]))
# print(dp)
print(max(dp))