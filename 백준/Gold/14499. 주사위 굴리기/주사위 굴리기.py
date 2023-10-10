import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split())) # 1 : 동, 2 : 서, 3 : 북, 4 : 남

dice = [0 for _ in range(6)] # idx 0 : 위, idx 1 : 동, idx 2 : 서, idx 3 : 북, idx 4 : 남, idx 5 : 바닥

def turn(lst, ord, x, y):
    new_list = [0 for _ in range(6)] # idx 0 : 위, idx 1 : 동, idx 2 : 서, idx 3 : 북, idx 4 : 남, idx 5 : 바닥
    if ord == 1:
        new_list[0] = lst[2]
        new_list[1] = lst[0]
        new_list[2] = lst[5]
        new_list[3] = lst[3]
        new_list[4] = lst[4]
        new_list[5] = lst[1]
        y += 1
    elif ord == 2:
        new_list[2] = lst[0]
        new_list[0] = lst[1]
        new_list[5] = lst[2]
        new_list[3] = lst[3]
        new_list[4] = lst[4]
        new_list[1] = lst[5]
        y -= 1
    elif ord == 3:
        new_list[0] = lst[4]
        new_list[1] = lst[1]
        new_list[2] = lst[2]
        new_list[3] = lst[0]
        new_list[4] = lst[5]
        new_list[5] = lst[3]
        x -= 1
    else:
        new_list[4] = lst[0]
        new_list[1] = lst[1]
        new_list[2] = lst[2]
        new_list[0] = lst[3]
        new_list[5] = lst[4]
        new_list[3] = lst[5]
        x += 1
    if x >= N or x < 0 or y >= M or y < 0:
        return False
    return [new_list, x, y]

for i in range(-1, len(order)):
    if i == -1:
        if not matrix[x][y]:
            matrix[x][y] = dice[5]
        else:
            dice[5] = matrix[x][y]
            matrix[x][y] = 0
        continue
    order_num = order[i]
    check = turn(dice, order_num, x, y)
    if not check:
        continue
    dice, x, y = check[0], check[1], check[2]
    if not matrix[x][y]:
        matrix[x][y] = dice[5]
    else:
        dice[5] = matrix[x][y]
        matrix[x][y] = 0
    print(dice[0])