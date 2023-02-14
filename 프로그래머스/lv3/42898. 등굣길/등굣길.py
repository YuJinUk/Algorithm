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
    # 시간초과 산물
    # dp = [[] for _ in range(n + m - 1)] # 지나치는 순서에 따른 모든 리스트를 생성한 dp 
    # dp[0].append(start)
    # for i in range(1, len(dp)):
    #     for x, y in dp[i-1]:
    #         if x+1<=m and [x+1, y] not in puddles:
    #             dp[i].append((x+1,y))
    #         if y+1<=n and [x, y+1] not in puddles:
    #             dp[i].append((x,y+1))
    # return len(dp[-1]) 
    
    # dfs로 탐색하면 시간초과
    # result = 0
    # print(dp)
    # while dp:
    #     x, y = dp.popleft()
    #     if x == m and y == n:
    #         result += 1
    #         continue
    #     if x+1<=m and [x+1, y] not in puddles:
    #         dp.append((x+1, y))
    #     if y+1<=n and [x, y+1] not in puddles:
    #         dp.append((x, y+1))
    # return result%(10**9 +7)
