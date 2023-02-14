def board(x, y, m):
    result = 0
    for i in range(x, x +m):
        for j in range(y, y + m):
            result += matrix[i][j]
    return result

T = int(input())
for tt in range(1, T+1):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    ans = []
    for i in range(n-m+1):
        for j in range(n-m+1):
            ans.append(board(i, j, m))
    print(f'#{tt} {max(ans)}')