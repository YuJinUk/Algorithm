def check(n, boards):
    b = sum(boards, [])
    if b.count('o') < 5:
        return 0
    
    r_idx = []
    for i in range(n*n):
        if b[i] == 'o':
            r_idx.append(list(divmod(i, n)))
    def check_2(a, b):
        direction = [(1,1),(1,-1),(1,0),(0,1)]
        for dx, dy in direction:
            x, y = a, b
            cnt = 1
            while True:
                nx = x+dx
                ny = y+dy
                if -1<nx<n and -1<ny<n and board[nx][ny] == 'o':
                    cnt += 1
                    x = nx
                    y = ny
                else:
                    break
                if cnt == 5:
                    return 1
        else:
            return 0
    result = []

    for x, y in r_idx:
        result.append(check_2(x, y))
    
    if sum(result):
        return 1
    return 0

T = int(input())
for tt in range(1, T+1):
    n = int(input())
    board = [list(input().rstrip()) for _ in range(n)]
    answer = check(n, board)
    if answer:
        print(f'#{tt} YES')
    else:
        print(f'#{tt} NO')