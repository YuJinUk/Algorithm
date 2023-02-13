T = int(input())
for tt in range(1, T+1):
    matrix = [list(map(int, input().split())) for _ in range(9)]
    columns = []
    for i in range(len(matrix)):
        column = []
        for j in range(len(matrix)):
            column.append(matrix[j][i])
        columns.append(column)
    matrix += columns
    box = [[],[],[]]
    for i in range(9):
        for j in range(3):
            box[0].append(matrix[i][j])
            box[1].append(matrix[i][j+3])
            box[2].append(matrix[i][j+6])
        if len(box[0]) == 9:
            matrix += box
            box = [[],[],[]]
    for sudo in matrix:
        if len(sudo) != len(set(sudo)):
            print(f'#{tt} 0')
            break
    else:
        print(f'#{tt} 1')