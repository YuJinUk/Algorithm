n, k = map(int, input().split())
num = [list(map(int, input().split())) for _ in range(n)] # 여자 0 남자 1 / 학년 1~6

girl = [0 for _ in range(6)]
boy = [0 for _ in range(6)]

for peo in num:
    if peo[0] == 0:
        girl[peo[1]-1] += 1
    else:
        boy[peo[1]-1] += 1

room_girl = [(i-1)//k +1 for i in girl if i != 0]
room_boy = [(j-1)//k +1 for j in boy if j != 0]

print(sum(room_girl) + sum(room_boy))