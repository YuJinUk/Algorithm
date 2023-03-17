r, c, w = map(int, input().split())
dp = [[1], [1,1]]
for i in range(2, r+w+1):
    lst = [1]
    for j in range(len(dp[i-1])-1):
        lst.append(dp[i-1][j] + dp[i-1][j+1])
    lst.append(1)
    dp.append(lst)
answer = 0
for i in range(w):
    for j in range(i+1):
        answer += dp[r-1+i][c-1+j]
print(answer)