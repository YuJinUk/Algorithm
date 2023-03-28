dp = [[1,0],[0,1],[1,1]]
for i in range(3, 41):
    dp.append([dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]])

t = int(input())
for tt in range(1, t+1):
    n = int(input())
    print(*dp[n])