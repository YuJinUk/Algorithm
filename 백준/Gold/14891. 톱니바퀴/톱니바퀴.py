import sys
from collections import deque
input = sys.stdin.readline

clock = [deque(list(map(int, input().rstrip()))) for _ in range(4)] # N극 : 0, S극 : 1

K = int(input().rstrip())
order = [list(map(int, input().split())) for _ in range(K)]

for cloc, direction in order:
    check = [] # 2 : 왼쪽, 6 : 오른쪽 톱니
    for i in range(4):
        check.append((clock[i][2], clock[i][6]))
    cloc -= 1 # 시계번호 -> index 번호
    if cloc > 0 : # 좌측 시계 바꾸기
        for i in range(cloc, 0, -1): # 한 칸씩 좌측으로 이동
            if check[i - 1][0] != check[i][1]: # 좌측 시계의 오른쪽, 우측 시계의 왼쪽
                if not (cloc - i + 1) % 2:
                    clock[i - 1].rotate(direction)
                else: # 홀수면 하나 넘어서
                    clock[i - 1].rotate((-1) * direction)
            else:
                break
    if cloc < 3 : # 우측 시계 바꾸기
        for i in range(cloc, 3): # 한 칸씩 우측으로 이동
            if check[i][0] != check[i + 1][1]: # 좌측 시계의 오른쪽, 우측 시계의 왼쪽
                if not (i + 1 - cloc) % 2:
                    clock[i + 1].rotate(direction)
                else:
                    clock[i + 1].rotate((-1) * direction)
            else:
                break
    clock[cloc].rotate(direction)

answer = 0
for i in range(4):
    answer += clock[i][0] * (2 ** i)

print(answer)