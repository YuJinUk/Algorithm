from sys import stdin
lcs1 = stdin.readline().rstrip()
lcs2 = stdin.readline().rstrip()
lcs3 = stdin.readline().rstrip()
dp = [[[0] * (len(lcs3)+1) for _ in range(len(lcs2)+1)] for _ in range(len(lcs1)+1)]
for i in range(1, len(lcs1)+1):
    for j in range(1, len(lcs2)+1):
        for k in range(1, len(lcs3)+1):
            # 3개의 문자가 같을 경우
            if lcs1[i-1] == lcs2[j-1] == lcs3[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            # 다를 경우
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

print(dp[-1][-1][-1])