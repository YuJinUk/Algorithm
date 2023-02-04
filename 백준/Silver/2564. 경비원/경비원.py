# 북 1 / 남 2 / 서 3 / 동 4
# input : 1줄 - 가로와 세로 / 2줄 - 상점의 개수 / 동 or 서는 위에서부터의 거리 남 or 북은 왼쪽에서부터의 거리
x, y = map(int, input().split())
n = int(input())
store = [list(map(int, input().split())) for _ in range(n)]
me = list(map(int, input().split()))

my_location = me[0]
distance = 0
for i in range(len(store)):
    store_location = store[i][0]
    if my_location == store_location :
        distance += abs(me[1]- store[i][1])
    elif my_location in [1,2]:
        if store_location in [1,2]:
            distance += y
            if me[1] + store[i][1] < x:
                distance += me[1] + store[i][1]
            else:
                distance += x*2 -me[1] - store[i][1]
        elif store_location == 3:
            distance += me[1]
            if my_location == 1:
                distance += store[i][1]
            else:
                distance += y - store[i][1]
        else:
            distance += x - me[1]
            if my_location == 1:
                distance += store[i][1]
            else:
                distance += y - store[i][1]
    else :
        if store_location in [3,4]:
            distance += x
            if me[1] + store[i][1] < y:
                distance += me[1] + store[i][1]
            else:
                distance += y*2 -me[1] - store[i][1]
        elif store_location == 1:
            distance += me[1]
            if my_location == 3:
                distance += store[i][1]
            else:
                distance += x - store[i][1]
        else:
            distance += y - me[1]
            if my_location == 3:
                distance += store[i][1]
            else:
                distance += x - store[i][1]
print(distance)