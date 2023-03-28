import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
coin.sort()
dp = [0] * (k+1)
dp[0] = 1
for i in coin:
    if i > k:
        break
    dp[i] += 1
    for j in range(k+1):
        if j > i:
            dp[j] += dp[j-i]
print(dp[-1])