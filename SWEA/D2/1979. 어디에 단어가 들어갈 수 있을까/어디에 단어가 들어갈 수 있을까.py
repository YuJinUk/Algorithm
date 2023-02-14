# 1979 어디에 단어가 들어갈 수 있을까.
T = int(input())
for tt in range(1, T+1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    columns = []
    for i in range(n):
        column = []
        for j in range(n):
            column.append(board[j][i])
        columns.append(column)
    board += columns
    result = []
    for boards in board:
        cnt = 0
        while boards:
            num = boards.pop(0)
            if not num and cnt:
                result.append(cnt)
                cnt = 0
                continue
            if num:
                cnt += 1
            if not boards and cnt:
                result.append(cnt)
    ans = 0
    for i in result:
        if i == m:
            ans += 1
    print(f'#{tt} {ans}')