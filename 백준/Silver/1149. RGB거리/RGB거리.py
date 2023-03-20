from sys import stdin
n = int(stdin.readline())
dp = list(map(int, stdin.readline().split()))
for _ in range(n-1):
    a, b, c = map(int, stdin.readline().split())
    a += min(dp[1],dp[2])
    b += min(dp[0],dp[2])
    c += min(dp[1],dp[0])
    dp = [a,b,c]
print(min(dp))