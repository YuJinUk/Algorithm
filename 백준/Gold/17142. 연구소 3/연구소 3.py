import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
board = deque()
v_list = deque()
cnt = 0
for i in range(n):
    row = list(map(int, input().rstrip().split()))
    for j in range(n):
        if row[j] == 2:
            v_list.append((i,j))
        elif row[j] == 1:
            row[j] = -1
            cnt += 1
    board.append(row)
    
def bfs(visit):
    global v_list
    dxdy = [(1,0),(-1,0),(0,-1),(0,1)]
    check = [[-1 for _ in range(n)] for _ in range(n)]
    visited = deque()
    for x, y in visit:
        check[x][y] = 1
        visited.append((x,y))
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
    for alpha, beta in v_list:
        if (alpha, beta) not in visited and check[alpha][beta] == -1:
            check[alpha][beta] = -2
            
    check = sum(check, [])
    if check.count(-1) == cnt:
        return max(check)-1
    else:
        return float('inf')

result = deque()
for c in combinations(v_list, m):
    result.append(bfs(c))
if list(set(result))[0] == float('inf'):
    print(-1)
else:
    print(min(result))