n = int(input())
dp = [0] + [1] * 9
nxtdp = [0]*10
if n == 1:
    print(9)
    exit()
for _ in range(1, n):
    for i in range(10):
        if i != 0 and i != 9:
            nxtdp[i] = dp[i+1] + dp[i-1]
        elif not i:
            nxtdp[i] = dp[i+1]
        elif i == 9:
            nxtdp[i] = dp[i-1]
    for idx, i in enumerate(nxtdp):
        dp[idx] = i
print(sum(dp)%int(1e9))