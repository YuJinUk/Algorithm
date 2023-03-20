from sys import stdin
from collections import deque
n, m = map(int, stdin.readline().split())
board = [list(stdin.readline().rstrip()) for _ in range(n)]
dxdy = [(1,0),(-1,0),(0,1),(0,-1)]
start = (0,0)
queue = deque()
queue.append(start)
while queue:
    x, y = queue.popleft()
    for dx, dy in dxdy:
        nx = x + dx
        ny = y + dy
        if -1<nx<n and -1<ny<m and board[nx][ny] == '1':
            board[nx][ny] = int(board[x][y]) + 1
            queue.append((nx, ny))
print(board[-1][-1])