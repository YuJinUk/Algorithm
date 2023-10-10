import sys
input = sys.stdin.readline

N = int(input().rstrip())
matrix = [list(map(int, input().split())) for _ in range(N)]

# d1 + d2 - 1
def f(x, y, d1, d2):
    board = [[0] * N for _ in range(N)]
    if x + d1 + d2 > N - 1 or y - d1 < -1 or y + d2 > N - 1:
        return int(1e9)
    for i in range(d1+1):
        board[x + i][y - i] = 5
        board[x + d2 + i][y + d2 - i] = 5
    for j in range(d2+1):
        board[x + j][y + j] = 5
        board[x + d1 + j][y - d1 + j] = 5
    for idx, i in enumerate(board):
        if i.count(5) == 2:
            cnt = 0
            for kdx, k in enumerate(i):
                if k == 5: cnt += 1
                elif cnt == 1: board[idx][kdx] = 5
                if cnt == 2: break
        for jdx, j in enumerate(i):
            if board[idx][jdx] == 5: continue
            if 0 <= idx < x + d1 and 0 <= jdx <= y: board[idx][jdx] = 1
            elif 0 <= idx <= x + d2 and y < jdx <= N-1: board[idx][jdx] = 2
            elif x + d1 <= idx <= N-1 and 0 <= jdx < y - d1 + d2: board[idx][jdx] = 3
            elif x + d2 < idx <= N-1 and y - d1 + d2 <= jdx <= N-1: board[idx][jdx] = 4
            else: board[idx][jdx] = 5
    result = [0 for _ in range(6)]
    for idx, row in enumerate(board):
        for jdx, col in enumerate(row):
            result[col] += matrix[idx][jdx]
    result = result[1:]
    if 0 in result:
        return float('inf')
    return max(result) - min(result)

answer = float('inf')
for i in range(N):
    for j in range(N):
        for k in range(N):
            for l in range(N):
                answer = min(answer, f(i, j, k, l))
print(answer)