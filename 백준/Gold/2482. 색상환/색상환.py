import sys
input = sys.stdin.readline

N = int(input().rstrip())
K = int(input().rstrip())

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(N + 1):
    dp[i][0] = 1; dp[i][1] = i

for i in range(2, N + 1):
    for j in range(2, K + 1):
        if i == N : dp[i][j] = dp[i-3][j-1] + dp[i-1][j] # 왼쪽 : i번째를 선택했을 때, 오른쪽 : 선택 안했을 때
        else : dp[i][j] = dp[i-2][j-1] + dp[i-1][j]
        dp[i][j] %= int(1e9) + 3
print(dp[-1][-1])