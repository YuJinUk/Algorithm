from sys import stdin
lcs1 = stdin.readline().rstrip()
lcs2 = stdin.readline().rstrip()
dp = [0] * len(lcs2)
dp2 = [""] * len(lcs2)
for i in range(len(lcs1)):
    check = 0
    w = ''
    for j in range(len(lcs2)):
        if check < dp[j]:
            check = dp[j]
            w = dp2[j]
        elif lcs1[i] == lcs2[j]:
            dp[j] = check + 1
            dp2[j] = w + lcs2[j]
        # print(dp)
        # print(dp2)
# print(dp)
# print(dp2)
max_v = max(dp)
print(max_v)
print(dp2[dp.index(max_v)])