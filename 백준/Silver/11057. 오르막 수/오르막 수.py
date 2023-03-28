n = int(input())
dp = [1] * 10
# print(dp)
if n == 1:
    print(10)
    exit()
for _ in range(1, n):
    nxtdp = [0]*10
    for i in range(10):
        if i:
            for j in range(i+1):
                nxtdp[i] += dp[j]
        else:
            nxtdp[i] = dp[i]
    for idx, i in enumerate(nxtdp):
        dp[idx] = i
    # print(dp)
print(sum(dp)%(int(1e4)+7))