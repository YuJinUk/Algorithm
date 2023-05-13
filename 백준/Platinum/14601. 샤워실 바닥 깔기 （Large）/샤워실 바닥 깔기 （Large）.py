import sys
input = sys.stdin.readline

K = int(input())
x, y = map(int, input().split())

cnt = 0
l = 2 ** K
x, y = l - y, x - 1
matrix = [[0] * l for _ in range(l)]
matrix[x][y] = -1

def check0(a, b, c):
    for i in range(a, a+c):
        for j in range(b, b+c):
            if matrix[i][j]:
                return 0
    return 1

# def dfs(nx, ny, nz, cnt):
#     # print('nxnynzcnt', nx, ny, nz, cnt)
#     cnt += 1
#     half = nz//2
#     if check0(nx, ny, half):
#         matrix[nx -1 + half][ny -1 + half] = cnt
#     if check0(nx, ny + half, half):
#         matrix[nx -1 + half][ny + half] = cnt
#     if check0(nx + half, ny, half):
#         matrix[nx + half][ny -1 + half] = cnt
#     if check0(nx + half, ny + half, half):
#         matrix[nx + half][ny + half] = cnt
#     # print(matrix)
#     if half == 2:
#         return
    
#     dfs(nx, ny, half, cnt)
#     dfs(nx, ny + half, half, cnt)
#     dfs(nx + half, ny, half, cnt)
#     dfs(nx + half, ny + half, half, cnt)

def dfs(x, y, z):
    global cnt
    cnt += 1
    half = z//2
    pos = [[x - 1 + half, y - 1 + half], [x + half, y - 1 + half], [x - 1 + half, y + half], [x + half, y + half]]
    for idx, value in enumerate([[x, y], [x + half, y], [x, y + half], [x + half, y + half]]):
        nx,ny = value
        dx,dy = pos[idx]
        if check0(nx,ny,half):
            matrix[dx][dy] = cnt
    if z == 2:
        return
    
    dfs(x, y, half)
    dfs(x + half, y, half)
    dfs(x, y + half, half)
    dfs(x + half, y + half, half)


dfs(0, 0, l)
# print(matrix)
for i in matrix:
    print(*i)