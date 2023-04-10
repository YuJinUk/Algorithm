import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
matrix, fish, shark = [], [], []
for idx in range(n):
    lin = list(map(int, input().split()))
    for jdx, j in enumerate(lin):
        if j == 9 :
            shark.append((idx, jdx, 2, 0, 0))
            lin[jdx] = 0
        elif j :
            fish.append((idx, jdx, j))
    matrix.append(lin)

dxdy = [(-1, 0), (0, -1), (0, 1), (1, 0)]
queue = deque()
visit = [[False]*n for _ in range(n)]
queue.append(shark[0])
check, check_dist = [], float('inf')
result = 0
aa = []
while queue:
    shark_x, shark_y, shark_size, cnt, ans = queue.popleft()
    fish.sort(key = lambda x: x[-1])
    if fish and fish[0][-1] >= shark_size:
        # print('먹을게 없음')
        print(ans)
        exit()
    elif not fish:
        # print('다먹음')
        print(ans)
        exit()
    for dx, dy in dxdy:
        nx = shark_x + dx
        ny = shark_y + dy
        if -1 < nx < n and -1 < ny < n and not visit[nx][ny]:
            visit[nx][ny] = True
            if matrix[nx][ny] > shark_size:
                continue
            elif matrix[nx][ny] == shark_size:
                queue.append((nx, ny, shark_size, cnt, ans + 1))
            elif 0 < matrix[nx][ny] < shark_size:
                if check_dist > ans:
                    check_dist = ans
                check.append((nx, ny, shark_size, cnt, ans))
                queue.append((nx, ny, shark_size, cnt, ans + 1))
                visit = [[False]*n for _ in range(n)]
                # print(check_dist)
            elif not matrix[nx][ny]:
                queue.append((nx, ny, shark_size, cnt, ans + 1))
            if check_dist + 1 == ans:
                check.sort(key = lambda x: (x[-1], x[0], x[1]))
                # print('11111111111',nx, ny, shark_size, ans)
                # print(check)
                nxx, nyy, shark_size, cnt, ans = check[0]
                fish.remove((nxx, nyy, matrix[nxx][nyy]))
                matrix[nxx][nyy] = 0
                if cnt + 1 == shark_size:
                    shark_size += 1
                    cnt = -1
                visit = [[False]*n for _ in range(n)]
                queue = deque()
                queue.append((nxx, nyy, shark_size, cnt + 1, ans+1))
                result += 1
                aa.append(ans + 1)
                check, check_dist = [], float('inf')
                # print((nxx, nyy, shark_size, ans + 1))
                break
    if not result and not queue:
        print(0)
        exit()
    # print(check_dist)
    # print(matrix)
    # print('check', check)
print(aa[-1])