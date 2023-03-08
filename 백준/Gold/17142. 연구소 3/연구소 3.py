from collections import deque
from itertools import combinations
n, m = map(int, input().split())
board = deque()
v_list = deque()
cnt = 0
for i in range(n):
    matrix = list(map(int, input().split()))
    for j in range(n):
        if matrix[j] == 2:
            v_list.append((i,j))
        elif matrix[j] == 1:
            matrix[j] = -1
            cnt += 1
    board.append(matrix)
def bfs(visit):
    dxdy = [(1,0),(-1,0),(0,-1),(0,1)]
    check = [[-1] * n for _ in range(n)]
    # for i in range(n):
    #     for j in range(n):
    #         if board[i][j] == 2:
    #             check[i][j] = 1
    #         elif board[i][j] == 0:
    #             check[i][j] = 0
    visited = deque()
    for x, y in visit:
        check[x][y] = 1
        visited.append((x,y))
    # print(check)
    visit = deque(visit)
    rm_list = deque()
    while visit:
        x, y = visit.popleft()
        for dx, dy in dxdy:
            nx = x + dx
            ny = y + dy
            if -1<nx<n and -1<ny<n and (nx,ny) not in visited:
                if board[nx][ny] == 0 and check[nx][ny] == -1 :
                    check[nx][ny] = check[x][y] + 1
                    visit.append((nx, ny))
                elif board[nx][ny] == 2 and check[nx][ny] == -1:
                    visit.append((nx, ny))
                    check[nx][ny] = check[x][y] + 1
                    rm_list.append((nx, ny))
    for a, b in rm_list:
        check[a][b] = 1

    check = sum(check,[])
    if check.count(-1) == cnt:
        return max(check)-1
    else:
        return float('inf')

result = deque()
for c in combinations(v_list, m):
    result.append(bfs(c))
if len(set(result)) == 1 and list(set(result))[0] == float('inf'):
    print(-1)
else:
    print(min(result))