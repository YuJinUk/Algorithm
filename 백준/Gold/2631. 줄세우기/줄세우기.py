import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
dp = [0 for _ in range(N)]
dp[0] = 1
result = 0
for i in range(1, N):
    for j in range(0, i):
        if nums[i] > nums[j] and result < dp[j]:
            result = dp[j]
    dp[i] = result + 1
    result = 0
print(N - max(dp)) 