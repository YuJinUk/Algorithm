def solution(triangle):
    n = len(triangle)
    dp = [[0]*n for _ in range(n)]
    dp[0][0] = triangle[0][0]

    for x in range(1, n):
        for y in range(len(triangle[x])):
            if y==0:
                dp[x][y] = triangle[x][0] + dp[x-1][0]
            elif x==y:
                dp[x][y] = triangle[x][y] + dp[x-1][y-1]
            else:
                dp[x][y] = max(triangle[x][y] + dp[x-1][y-1], triangle[x][y] + dp[x-1][y])

    return max(dp[-1])
