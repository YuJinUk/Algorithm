n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0][0] = tri[0][0]
for i in range(1, n):
    for j in range(i+1):
        if not j:
            dp[i][j] = tri[i][j] + dp[i-1][j]
        elif j == i:
            dp[i][j] = tri[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = max(tri[i][j] + dp[i-1][j], tri[i][j] + dp[i-1][j-1])
print(max(dp[-1]))