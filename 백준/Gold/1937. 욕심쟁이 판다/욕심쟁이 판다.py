import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(n)]
dxdy = [(1,0),(-1,0),(0,1),(0,-1)]

def dfs(start):
    x, y = start
    if dp[x][y] != -1:
        return dp[x][y]
    for dx, dy in dxdy:
        nx = x + dx
        ny = y + dy
        if -1 < nx < n and -1 < ny < n and matrix[x][y] < matrix[nx][ny]:
            check = dfs((nx, ny)) + 1
            if dp[x][y] < check:
                dp[x][y] = check
    return dp[x][y]

answer = -1
for i in range(n):
    for j in range(n):
        result = dfs((i, j))
        if answer < result:
            answer = result

print(answer + 2)