from math import factorial as fac
def solution(m, n, puddles):
    if not puddles:
        return fac(m+n-2)//(fac(m-1)*fac(n-1))
    start = (1,1)
    board = [[0]*(m+1) for _ in range(n+1)]
    board[1][1] = 1
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if 0<=i-1<=n and [j,i] not in puddles:
                board[i][j] += board[i-1][j]
            if 0<=j-1<=m and [j,i] not in puddles:
                board[i][j] += board[i][j-1]
    return board[-1][-1] % (10**9 +7)