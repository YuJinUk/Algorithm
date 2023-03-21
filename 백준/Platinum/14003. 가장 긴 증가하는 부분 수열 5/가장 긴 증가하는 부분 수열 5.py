# 이분 탐색
# 프로그래머스에 같은 문제 있음
from sys import stdin
n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
dp = [float('-inf')]
table = [(float('-inf'),0)]
for num in nums:
    if dp[-1] < num:
        dp.append(num)
        table.append((num, len(dp)-1))
    else:
        left = 0
        right = len(dp)
        while left < right:
            mid = (right + left) // 2
            if dp[mid] < num:
                left = mid + 1
            else:
                right = mid
        dp[right] = num
        table.append((num, right))
# print(dp)
# print(table)
m = len(dp) - 1
print(m)
result = []
for i in range(len(table)-1, 0, -1):
    if m == table[i][1]:
        result.append(table[i][0])
        m -= 1
result.reverse()
print(*result)