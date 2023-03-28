from collections import deque
def solution(x, y):
    # 끝까지 갔으면 길이 있으므로 1을 return
    if (x, y) == (n-1, m-1):
        return 1

    # 방문한 적이 없으면 탐색
    if dp[x][y] == -1:
        dp[x][y] = 0
        for dx, dy in dxdy:
            nx = x + dx 
            ny = y + dy
            if -1 < nx < n and -1 < ny < m and board[x][y] > board[nx][ny]:
                dp[x][y] += solution(nx, ny)

    return dp[x][y]

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*m for _ in range(n)]
dxdy = [(1,0),(0,1),(-1,0),(0,-1)]
print(solution(0,0))