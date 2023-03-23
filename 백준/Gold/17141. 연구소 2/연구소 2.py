from collections import deque
from itertools import combinations
from sys import stdin
from copy import deepcopy
n, m = map(int, stdin.readline().split())
board = deque()
v_list = deque()
for i in range(n):
    matrix = list(map(int, stdin.readline().split()))
    for j in range(n):
        if matrix[j] == 2:
            v_list.append((i,j))
    board.append(matrix)

def bfs(v):
    dxdy = [(1,0),(-1,0),(0,-1),(0,1)]
    queue = deque(v)
    visited = [[-1]* n  for _ in range(n)]
    answer = 0
    for x,y in queue:
        visited[x][y] = 0
    while queue:
        x,y = queue.popleft()
        for dx, dy in dxdy:
            nx = x + dx
            ny = y + dy
            if -1 < nx < n and -1 < ny < n:
                if visited[nx][ny] == -1 and board[nx][ny] != 1:
                    queue.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
                    answer = max(answer,visited[x][y] + 1)
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1 and board[i][j] != 1:
                return float("inf")
    return answer
# print(v_list)
result = float('inf')
for c in combinations(v_list, m):
    # board = deepcopy(board_d)
    ch = bfs(c)
    if result > ch:
        result = ch
    # print(c)
    # print(result)
if result == float('inf'):
    print(-1)
else:
    print(result)
