from copy import deepcopy
from sys import stdin
def move(board, direction):
    if direction == 0:  # 동쪽
        for i in range(n):
            top = n - 1
            for j in range(n - 2, -1, -1):
                if board[i][j]:
                    check = board[i][j]
                    board[i][j] = 0
                    if not board[i][top]:
                        board[i][top] = check
                    elif board[i][top] == check:
                        board[i][top] = check * 2
                        top -= 1
                    else:
                        top -= 1
                        board[i][top] = check
    elif direction == 1:  # 서쪽
        for i in range(n):
            top = 0
            for j in range(1, n):
                if board[i][j]:
                    check = board[i][j]
                    board[i][j] = 0
                    if not board[i][top]:
                        board[i][top] = check
                    elif board[i][top] == check:
                        board[i][top] = check * 2
                        top += 1
                    else:
                        top += 1
                        board[i][top] = check

    elif direction == 2:  # 남쪽
        for j in range(n):
            top = n - 1
            for i in range(n - 2, -1, -1):
                if board[i][j]:
                    check = board[i][j]
                    board[i][j] = 0
                    if not board[top][j]:
                        board[top][j] = check
                    elif board[top][j] == check:
                        board[top][j] = check * 2
                        top -= 1
                    else:
                        top -= 1
                        board[top][j] = check

    else: # 북쪽
        for j in range(n):
            top = 0
            for i in range(1, n):
                if board[i][j]:
                    check = board[i][j]
                    board[i][j] = 0
                    if not board[top][j]:
                        board[top][j] = check
                    elif board[top][j] == check:
                        board[top][j] = check * 2
                        top += 1
                    else:
                        top += 1
                        board[top][j] = check
    return board

def dfs(board, cnt):
    global answer
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                if board[i][j] > answer:
                    answer = board[i][j]
        return
    for i in range(4):
        board_copy = deepcopy(board)
        nxt_board = move(board_copy, i)
        dfs(nxt_board, cnt + 1)
        
n = int(stdin.readline())
matrix = [list(map(int, stdin.readline().split())) for _ in range(n)]
answer = 0
dfs(matrix, 0)
print(answer)