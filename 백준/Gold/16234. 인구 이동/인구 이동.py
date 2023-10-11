import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().rstrip().split())

matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]

def solution(answer):
    checkboard = [[-1] * N for _ in range(N)]
    v = deque()

    def f(visit, x, y, idx):
        dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visit.append((x, y))
        checkboard[x][y] = idx
        cnt = 1
        cumulative = deque()
        cumulative.append(matrix[x][y])
        national = deque()
        national.append((x, y))
        while visit:
            x, y = visit.pop()
            for dx, dy in dxdy:
                nx, ny = x + dx, y + dy
                if -1 < nx < N and -1 < ny < N and checkboard[nx][ny] != idx:
                    gap = abs(matrix[nx][ny] - matrix[x][y])
                    if L <= gap <= R:
                        cumulative.append(matrix[nx][ny])
                        national.append((nx, ny))
                        checkboard[nx][ny] = idx
                        visit.append((nx, ny))
                        cnt += 1
        return cumulative, national, cnt

    flag, idx, dic = 0, 0, {}
    for i in range(N):
        for j in range(N):
            if checkboard[i][j] == -1:
                cum, nation, cnt = f(v, i, j, idx)
                dic[idx] = [cum, nation, cnt]
                idx += 1

    check = 0
    for i in range(idx):
        vallist, national, l = dic[i]
        val = sum(vallist)
        if l > 1:
            check += 1
            for x, y, in national:
                matrix[x][y] = val // l
    if check: answer += 1
    return answer

answer = 0
while True:
    result = solution(answer)
    if result == answer: print(answer); break
    answer = result