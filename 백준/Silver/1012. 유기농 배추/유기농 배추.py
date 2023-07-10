import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    board = [[False] * m for _ in range(n)]
    check = []
    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = True
        check.append((y, x))
    # print(board)
    
    dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque()
    start = (y, x)
    queue.append(start)
    board[y][x] = False
    answer = 0
    while True:
        try:
            y, x = queue.pop()
        except IndexError:
            answer += 1
            if check:
                queue.append(check[0])
            else:
                break
            continue
        if (y, x) not in check:
            continue
        check.remove((y, x))
        for dx, dy in dxdy:
            nx = x + dx
            ny = y + dy
            if -1 < nx < m and -1 < ny < n and board[ny][nx] and (ny, nx) in check:
                queue.append((ny, nx))
                board[ny][nx] = False
    print(answer)