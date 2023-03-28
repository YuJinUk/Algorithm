from sys import stdin
input = stdin.readline
n = int(input())
p = [0] + list(map(int, input().split()))
dp = [i for i in p]
for i in range(1, n+1):
    for idx in range(1, len(p)):
        if i > idx:
            dp[i] = max(dp[i], dp[i-idx] + dp[idx])
        # print(dp[i])
    # print(dp)
print(dp[-1])