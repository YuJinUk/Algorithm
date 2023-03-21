from sys import stdin
lcs1 = stdin.readline().rstrip()
lcs2 = stdin.readline().rstrip()
dp = [0] * len(lcs2)
for i in range(len(lcs1)):
    check = 0
    for j in range(len(lcs2)):
        if check < dp[j]:
            check = dp[j]
        elif lcs1[i] == lcs2[j]:
            dp[j] = check + 1
# print(dp)
print(max(dp))