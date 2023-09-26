import sys
input = sys.stdin.readline
N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
maxnum = float('inf')
answer = float('inf')

for i in range(3):
    dp = [[maxnum] * 3 for _ in range(N)]
    dp[0][i] = matrix[0][i]
    for j in range(1, N):
        for k in range(3):
            dp[j][k] = matrix[j][k] + min(dp[j-1][:k] + dp[j-1][k+1:])
    for k in range(3):
        if i != k: answer = min(answer, dp[-1][k])
print(answer)