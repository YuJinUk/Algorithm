import sys
input = sys.stdin.readline

N = int(input())
if N == 1: print(3); sys.exit(0)
if N == 2: print(7); sys.exit(0)
dp = [1, 3, 7] + [0 for _ in range(N-2)]
for i in range(3,N+1):
    dp[i] = (dp[i-2] + dp[i-1]*2) % 9901
print(dp[-1])