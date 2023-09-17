import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
check = [i - 1 for i in range(n + 1)]
check[0] = 0

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if not i % 2 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1
        check[i] = i//2
    if not i % 3 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1
        check[i] = i//3
        
print(dp[-1])
print(n, end = " ")
while check[n] != 0:
    print(check[n], end = " ")
    n = check[n]