import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())
matrix = [[0] * N for _ in range(N)]

K = int(input().rstrip())
apple = []
for _ in range(K):
    x, y = map(int, input().split())
    matrix[x - 1][y - 1] = 1
    apple.append((x, y))

M = int(input().rstrip())
move = {}
for _ in range(M):
    x, y = input().split()
    move[int(x)] = y
dxdy = {0 : (0, 1),
        1 : (1, 0),
        2 : (0, -1),
        3 : (-1, 0)}

direction, time = 0, 0
row, col = 0, 0
matrix[row][col] = -1
visit = deque()
visit.append((row, col))
while True:
    time += 1
    dx, dy = dxdy[direction]
    nx, ny = row + dx, col + dy
    if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
        break
    if matrix[nx][ny] == 1:
        matrix[nx][ny] = -1
        visit.append((nx, ny))
        row, col = nx, ny
    elif not matrix[nx][ny]:
        matrix[nx][ny] = -1
        visit.append((nx, ny))
        rx, ry = visit.popleft()
        matrix[rx][ry] = 0
        row, col = nx, ny
    else:
        break
    if time in move:
        if move[time] == "D":
            direction += 1 ;direction %= 4
        else:
            direction -= 1
            if direction < 0: direction += 4
            direction %= 4

print(time)