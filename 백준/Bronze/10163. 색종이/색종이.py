paper = int(input())
n = [list(map(int, input().split())) for _ in range(paper)]

board = [[0]* 1001 for _ in range(1001)]

for idx, k in enumerate(n):
    for i in range(k[0], k[0] + k[2]):
        for j in range(k[1], k[1] + k[3]):
            board[i][j] = idx+1

board_new = []
for i in board:
    for j in i:
        if j != 0:
            board_new.append(j)

for i in range(1,paper+1):
    print(board_new.count(i))