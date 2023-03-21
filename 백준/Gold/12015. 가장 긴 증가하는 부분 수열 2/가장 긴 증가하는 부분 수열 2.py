# 이분 탐색
# 프로그래머스에 같은 문제 있음
from sys import stdin
n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
dp = [0]
for num in nums:
    if dp[-1] < num:
        dp.append(num)
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
print(len(dp)-1)