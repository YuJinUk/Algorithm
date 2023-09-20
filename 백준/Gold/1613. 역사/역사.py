import sys
input = sys.stdin.readline

N, K = map(int, input().split())
matrix = [[False for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(K):
    a, b = map(int, input().split())
    matrix[a][b] = True

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if matrix[i][k] and matrix[k][j]:
                matrix[i][j] = True

s = int(input())
for _ in range(s):
    x, y = map(int, input().split())
    if matrix[x][y]: print(-1)
    elif matrix[y][x]: print(1)
    else: print(0)