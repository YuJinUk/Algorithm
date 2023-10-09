import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split()) # 0: 북, 1: 동, 2: 남, 3: 서
matrix = [list(map(int, input().split())) for _ in range(N)] # 1: 벽, 0: 청소x

start = deque()
start.append((r, c))
dxdy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
matrix[r][c] = -1
answer = 1
while True:
    x, y = start.popleft()
    checkaround = 0
    for i in range(4):
        d = (d + 3) % 4
        dx, dy = dxdy[d]
        nx, ny = x + dx, y + dy
        if -1 < nx < N and -1 < ny < M and not matrix[nx][ny]:
            matrix[nx][ny] = -1
            answer += 1
            start.append((nx, ny))
            checkaround += 1
            break
    if not checkaround:
        dx, dy = dxdy[d]
        nx, ny = x + (-1) * dx, y + (-1) * dy
        if -1 < nx < N and -1 < ny < M and matrix[nx][ny] == 1:
            print(answer)
            sys.exit(0)
        else:
            start.append((nx, ny))