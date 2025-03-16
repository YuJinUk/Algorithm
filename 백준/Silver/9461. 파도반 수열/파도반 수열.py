dp1 = [1, 2, 3]
dp2 = [1, 1, 2]
i = 3
while i < 51:
    dp2.append(dp1[i - 3] + dp1[i - 1])
    dp1.append(dp2[i] + dp2[i - 2])
    i += 1

# print(dp1)
# print(dp2)
t = int(input())
for tt in range(1, t + 1):
    n = int(input())
    if n % 2:
        print(dp2[n // 2])
    else:
        print(dp1[n // 2-1])