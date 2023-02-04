x, y = map(int, input().split())
n = int(input())
scissor = [list(map(int, input().split())) for _ in range(n)] + [[0,0], [0,y] ,[1,0], [1,x]]
scissor.sort()
row, column = 0, 0
for i in range(len(scissor)-1):
    if scissor[i][0] == 0 and scissor[i][1] < y:
        max_row = scissor[i+1][1]-scissor[i][1]
        if row < max_row:
            row = max_row
    elif scissor[i][0] == 1 and scissor[i][1] < x:
        max_col = scissor[i+1][1]-scissor[i][1]
        if column < max_col:
            column = max_col
print(row * column)