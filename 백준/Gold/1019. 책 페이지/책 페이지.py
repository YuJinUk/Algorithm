n = int(input())
dp = [0] * 10
a = 1
while n>0:
    while n%10 != 9:
        for i in str(n):
            dp[int(i)] += a
        n -= 1
    if n < 10:
        for i in range(n+1):
            dp[i] += a
    else:
        for i in range(10):
            dp[i] += (n//10+1) * a
    dp[0] -= a
    n = n // 10
    a *= 10
print(*dp)