import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

def dfs(check_board):
    dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    virus = deque()
    checkboard = deepcopy(check_board)
    for idx, i in enumerate(checkboard):
        for jdx, j in enumerate(i):
            if j == 2:
                virus.append((idx, jdx))
    while virus:
        x, y = virus.pop()
        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy
            if -1 < nx < N and -1 < ny < M and not checkboard[nx][ny]:
                checkboard[nx][ny] = 2
                virus.append((nx, ny))
    result = sum(checkboard, []).count(0)
    return result

def gen_combinations(arr, n):
    result = []

    if n == 0:
        return [[]]

    for i in range(0, len(arr)):
        elem = arr[i]
        rest_arr = arr[i + 1:]
        for C in gen_combinations(rest_arr, n - 1):
            result.append([elem] + C)

    return result

def f(board):
    global answer
    No = []
    for i in range(N):
        for j in range(M):
            if not board[i][j]:
                No.append((i, j))
    comb = gen_combinations(No, 3)
    for i in comb:
        for x, y in i:
            board[x][y] = 1
        answer = max(answer, dfs(board))
        for x, y in i:
            board[x][y] = 0


N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
answer = 0
f(matrix)
print(answer)