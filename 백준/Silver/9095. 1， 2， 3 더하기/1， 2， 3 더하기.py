dp = [0, 1, 2, 4]
for i in range(4,11):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])
t = int(input())
for tt in range(1, t+1):
    n = int(input())
    print(dp[n])