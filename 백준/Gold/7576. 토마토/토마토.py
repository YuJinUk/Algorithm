from collections import deque
n, m = map(int, input().split())
matrix = deque()
queue = deque()
for i in range(m):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            queue.append((i,j))
    matrix.append(row)
dxdy = [(1,0),(-1,0),(0,1),(0,-1)]
while queue:
    x, y = queue.popleft()
    for dx, dy in dxdy:
        nx = x + dx
        ny = y + dy
        if -1<nx<m and -1<ny<n and not matrix[nx][ny]:
            matrix[nx][ny] = matrix[x][y] + 1
            queue.append((nx, ny))
check = sum(matrix,[])
if 0 not in check:
    print(max(check) -1)
else:
    print(-1)