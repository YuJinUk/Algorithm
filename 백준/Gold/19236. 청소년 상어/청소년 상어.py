import sys
from copy import deepcopy
input = sys.stdin.readline

# 물고기가 있는 지 확인하여 상어가 움직일 수 있는지 파악할 수 있는 함수
def check_fish(fish, num):
    for i in range(4):
        for j in range(4):
            if fish[i][j] == num:
                return (i, j)
    return False

# 물고기가 움직이는 함수
def move_fish(fish, info):
    for fish_number in range(1, 17): # 물고기는 1 ~ 16번까지 있음 / 번호가 작은게 먼저 움직임
        fish_location = check_fish(fish, fish_number)
        if not fish_location:
            continue
        x, y = fish_location
        moving = info[x][y]
        for _ in range(8):
            if moving > 8:
                moving -= 8
            dx, dy = direction[moving - 1]
            nx, ny = x + dx, y + dy
            if -1 < nx < 4 and -1 < ny < 4 and fish[nx][ny] >= 0:
                fish[x][y], fish[nx][ny] = fish[nx][ny], fish[x][y]
                info[x][y], info[nx][ny] = info[nx][ny], moving
                break
            moving += 1

# 상어가 갈 수 있는 곳 찾기
def move_shark(direct, x, y, fish):
    possible = []
    for _ in range(3):
        x += direction[direct - 1][0]
        y += direction[direct - 1][1]
        if -1 < x < 4 and -1 < y < 4 and fish[x][y] > 0:
            possible.append((x, y))
    return possible

# backtracking
def backtracking(fish, info, sharkx, sharky, eat_point):
    global answer
    fish = deepcopy(fish)
    info = deepcopy(info)
    eat_point += fish[sharkx][sharky]
    shark_direction = info[sharkx][sharky]
    fish[sharkx][sharky] = -1
    move_fish(fish, info)
    shark_possible = move_shark(shark_direction, sharkx, sharky, fish)

    if not shark_possible:
        answer = max(answer, eat_point)
        return
    for nx, ny in shark_possible:
        fish[sharkx][sharky] = 0
        info[sharkx][sharky] = 0
        backtracking(fish, info, nx, ny, eat_point)
        fish[sharkx][sharky] = -1
        info[sharkx][sharky] = shark_direction


fish, info = [[] for _ in range(4)], [[] for _ in range(4)]
for i in range(4):
    row = list(map(int, input().split()))
    for jdx, j in enumerate(row):
        if jdx % 2: info[i].append(j)
        else: fish[i].append(j)

answer = 0
direction = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
startx, starty = 0, 0

backtracking(fish, info, startx, starty, 0)
print(answer)