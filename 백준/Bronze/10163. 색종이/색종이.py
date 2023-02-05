paper = int(input())
n = [list(map(int, input().split())) for _ in range(paper)]
a = []
for i in n:
    a.append(max(i[0] + i[2], i[1]+i[3]))
b = max(a)
board = [[0]* (b+1) for _ in range(b+1)] # 가장 큰 맵을 기준으로 board를 생성

for idx, k in enumerate(n):
    for j in range(k[1], k[1] + k[3]):
        board[j][k[0]:k[0]+k[2]] = [idx+1] * k[2]

board_new = []
for i in board:
    for j in i:
        if j != 0:
            board_new.append(j)

for i in range(1,paper+1):
    print(board_new.count(i))
