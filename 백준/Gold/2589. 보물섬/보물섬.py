from collections import deque
n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]

def bfs(a, b):
    visit = [[0] * m for _ in range(n)]
    dxdy = [(1,0),(-1,0),(0,-1),(0,1)]
    v = deque()
    v.append([a, b])
    visit[a][b] = 1
    while v:
        x, y = v.popleft()
        for dx, dy in dxdy:
            nx = x + dx
            ny = y + dy
            if -1<nx<n and -1<ny<m and not visit[nx][ny] and matrix[nx][ny] == 'L':
                v.append([nx, ny])
                visit[nx][ny] = visit[x][y] + 1
    return max(sum(visit,[]))

answer = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'L':
            a = dfs(i,j)
            answer = a if answer < a else answer

print(answer-1)
