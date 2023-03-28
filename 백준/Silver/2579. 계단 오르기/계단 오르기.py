n = int(input())
nums = [0] + [int(input()) for _ in range(n)]
if n == 1:
    print(nums[1])
    exit()
elif n == 2:
    print(nums[1] + nums[2])
    exit()
dp = [0, nums[1], nums[1] + nums[2]]
for i in range(3, n+1):
    dp.append(max(dp[i-2] + nums[i], dp[i-3] + nums[i-1] + nums[i]))
print(dp[-1])