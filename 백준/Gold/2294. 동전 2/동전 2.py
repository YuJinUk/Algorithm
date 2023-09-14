import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]
coin.sort(reverse=True)

dp = [0] + [10001] * K

for num in coin:
    for i in range(num, K+1):
        dp[i] = min(dp[i],dp[i-num]+1)
if dp[-1] == 10001:
    print(-1)
else:
    print(dp[-1])