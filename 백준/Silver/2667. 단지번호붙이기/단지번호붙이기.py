from sys import stdin
from collections import deque
n = int(stdin.readline())
board = [list(map(int, stdin.readline().rstrip())) for _ in range(n)]

def dfs(x, y):
    dxdy = [(1,0),(-1,0),(0,1),(0,-1)]
    queue = deque()
    queue.append((x, y))
    board[x][y] = 0
    cnt = 1
    while queue:
        x, y = queue.pop()
        for dx, dy in dxdy:
            nx = x + dx
            ny = y + dy
            if -1<nx<n and -1<ny<n and board[nx][ny] == 1:
                cnt += 1
                board[nx][ny] = 0
                queue.append((nx, ny))
    return cnt

answer = sorted([dfs(i,j) for i in range(n) for j in range(n) if board[i][j]])
print(len(answer))
for i in answer:
    print(i)