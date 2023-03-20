n = int(input())
dp = [0] * (n+3)
dp[3], dp[5] = 1, 1
for i in range(3, n+1):
    if not dp[i-3] and dp[i-5]:
        dp[i] = dp[i-5] + 1
    elif dp[i-3] and not dp[i-5]:
        dp[i] = dp[i-3] + 1
    elif dp[i-3] and dp[i-5]:
        dp[i] = min(dp[i-3],dp[i-5]) + 1
print(dp[n] if dp[n] else -1)