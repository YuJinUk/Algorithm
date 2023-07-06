import sys
input = sys.stdin.readline
n = int(input())
dp = dict()
dp[1] = 0

def f(num):
    if num in dp:
        return dp[num]
    
    if (not num % 3) and (not num % 2):
        dp[num] = min(f(num//3) + 1, f(num//2) + 1)
    elif not num % 3:
        dp[num] = min(f(num-1) + 1, f(num//3) + 1)
    elif not num % 2:
        dp[num] = min(f(num-1) + 1, f(num//2) + 1)
    else:
        dp[num] = f(num-1) + 1
        
    return dp[num]

print(f(n))