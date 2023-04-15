nums = list(map(int, input().split()))
a, b = nums[0] * nums[1] / nums[2], nums[0] / nums[1] * nums[2]
print(int(max(a, b)))