from collections import deque
n = int(input())
matrix_N = deque()
matrix_W = deque()
B_list = deque()
R_list = deque()
G_list = deque()
for k in range(n):
    m = list(input())
    w = []
    matrix_N.append(m)
    for i in range(n):
        if m[i] == 'R':
            R_list.append([k,i])
            w.append('G')
        elif m[i] == 'B':
            B_list.append([k,i])
            w.append('B')
        else:
            G_list.append([k,i])
            w.append('G')
    matrix_W.append(w)

def dfs_n(visit,alpha):
    global cnt_n
    dxdy = [(1,0),(-1,0),(0,-1),(0,1)]
    visit = deque(visit)
    while visit:
        x, y = visit.pop()
        for dx, dy in dxdy:
            nx = x + dx
            ny = y + dy
            if -1<nx<n and -1<ny<n and not check[nx][ny] and matrix_N[nx][ny] == alpha:
                check[nx][ny] = True
                visit.append((nx,ny))
    cnt_n += 1
    return cnt_n

def dfs_w(visit,alpha):
    global cnt_w
    dxdy = [(1,0),(-1,0),(0,-1),(0,1)]
    visit = deque(visit)
    while visit:
        x, y = visit.pop()
        for dx, dy in dxdy:
            nx = x + dx
            ny = y + dy
            if -1<nx<n and -1<ny<n and not check[nx][ny] and matrix_W[nx][ny] == alpha:
                check[nx][ny] = True
                visit.append((nx,ny))
    cnt_w += 1
    return cnt_w

cnt_n = 0
cnt_w = 0
check = [[False] * n for _ in range(n)]
for i in B_list:
    if not check[i[0]][i[1]]:
        dfs_n([i], 'B')
for i in R_list:
    if not check[i[0]][i[1]]:
        dfs_n([i], 'R')
for i in G_list:
    if not check[i[0]][i[1]]:
        dfs_n([i], 'G')
check = [[False] * n for _ in range(n)]
for i in B_list:
    if not check[i[0]][i[1]]:
        dfs_w([i], 'B')
for i in G_list+R_list:
    if not check[i[0]][i[1]]:
        dfs_w([i], 'G')
print(cnt_n, cnt_w)