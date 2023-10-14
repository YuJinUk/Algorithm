import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline


# 기울이기
def move(x, y, direction_number):
    dx, dy = direction[direction_number]
    while True: # 공이 움직이지 않을 때까지 멈추지 못함
        x += dx
        y += dy
        if matrix[x][y] == 100:
            return x, y
        elif matrix[x][y] == -1:
            x -= dx
            y -= dy
            return x, y

# def sizecheck(a, b):
#     if a > b: return 0
#     elif a < b : return 1
#     else: return 2
# # slope 기준 red, blue 위치 체크
# def check(redx, redy, bluex, bluey, slope):
#     if not slope:
#         c = sizecheck(redy, bluey)
#     elif slope == 2:
#         c = sizecheck(redy, bluey)
#     elif slope == 1:
#         c = sizecheck(redx, bluex)
#     else:
#         c = sizecheck(redx, bluex)
#     if slope in [0, 3]:
#         if not c: return 1
#         elif c == 1: return 2
#         else: return 0
#     else:
#         if not c: return 2
#         elif c == 1: return 1
#         else: return 0

def backtracking(matrix, red, blue):
    queue = deque()
    visit = []
    redx, redy = red[0], red[1]
    bluex, bluey = blue[0], blue[1]
    queue.append((redx, redy, bluex, bluey))
    visit.append((redx, redy, bluex, bluey))
    answer = 0
    while queue:
        for _ in range(len(queue)):
            redx, redy, bluex, bluey = queue.popleft()
            if answer > 10:
                return -1
            if matrix[redx][redy] == 100 and matrix[bluex][bluey] != 100:
                return answer

            for slope in range(4):
                newredx, newredy = move(redx, redy, slope)
                newbluex, newbluey = move(bluex, bluey, slope)
                if matrix[newbluex][newbluey] == 100:
                    continue
                if (newredx, newredy) == (newbluex, newbluey):
                    if abs(newredx - redx) + abs(newredy - redy) > abs(newbluex - bluex) + abs(newbluey - bluey):
                        newredx -= direction[slope][0]; newredy -= direction[slope][1]
                    else:
                        newbluex -= direction[slope][0]; newbluey -= direction[slope][1]
                if (newredx, newredy, newbluex, newbluey) not in visit:
                    visit.append((newredx, newredy, newbluex, newbluey))
                    queue.append((newredx, newredy, newbluex, newbluey))
        answer += 1
    return -1

        # whofirst = check(redx, redy, bluex, bluey, slope)
        # if whofirst == 2:
        #     newbluex, newbluey = move(matrix, bluex, bluey, slope)
        #     if newbluex != 100:
        #         matrix[bluex][bluey], matrix[newbluex][newbluey] = matrix[newbluex][newbluey], matrix[bluex][bluey]
        #     else:
        #         bblue = matrix[bluex][bluey]
        #         matrix[bluex][bluey] = 0
        #     newredx, newredy = move(matrix, redx, redy, slope)
        #     if newredx != 100:
        #         matrix[redx][redy], matrix[newredx][newredy] = matrix[newredx][newredy], matrix[redx][redy]
        #     else:
        #         rred = matrix[redx][redy]
        #         matrix[redx][redy] = 0
        # else:
        #     newredx, newredy = move(matrix, redx, redy, slope)
        #     if newredx != 100:
        #         matrix[redx][redy], matrix[newredx][newredy] = matrix[newredx][newredy], matrix[redx][redy]
        #     else:
        #         rred = matrix[redx][redy]
        #         matrix[redx][redy] = 0
        #     newbluex, newbluey = move(matrix, bluex, bluey, slope)
        #     if newbluex != 100:
        #         matrix[bluex][bluey], matrix[newbluex][newbluey] = matrix[newbluex][newbluey], matrix[bluex][bluey]
        #     else:
        #         bblue = matrix[bluex][bluey]
        #         matrix[bluex][bluey] = 0
        # if (newredx, newredy, newbluex, newbluey) not in v:
        #     v.append((newredx, newredy, newbluex, newbluey))
        #     backtracking(matrix, (newredx, newredy), (newbluex, newbluey), slope_cnt + 1, v)
        #     v.pop()
        # if newredx != 100:
        #     matrix[redx][redy], matrix[newredx][newredy] = matrix[newredx][newredy], matrix[redx][redy]
        # else:
        #     matrix[redx][redy] = rred
        # if newbluex != 100:
        #     matrix[bluex][bluey], matrix[newbluex][newbluey] = matrix[newbluex][newbluey], matrix[bluex][bluey]
        # else:
        #     matrix[bluex][bluey] = bblue


N, M = map(int, input().split())

matrix = []
hole = []
red, blue, hole, wall = [], [], [], []
for idx in range(N):
    row = list(input().rstrip())
    for jdx, j in enumerate(row):
        if j == '#': wall.append((idx, jdx)); row[jdx] = -1
        elif j == 'R': red.append((idx, jdx)); row[jdx] = 1
        elif j == 'B': blue.append((idx, jdx)); row[jdx] = 2
        elif j == 'O': hole.append((idx, jdx)); row[jdx] = 100
        else: row[jdx] = 0
    matrix.append(row)
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 동 남 서 북
print(backtracking(matrix, red[0], blue[0]))