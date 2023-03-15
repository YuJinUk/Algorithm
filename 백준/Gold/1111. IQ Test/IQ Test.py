n = int(input())
nums = list(map(int, input().split()))
if n == 1:
    print('A')
    exit()
if n == 2:
    if nums[0] == nums[1]:
        print(nums[0])
    else:
        print('A')
    exit()
i,j,k = nums[0], nums[1], nums[2]
a = (k-j)//(j-i) if i != j else 0
b = k - a*j
for i in range(n-1):
    if nums[i] * a + b != nums[i+1]:
        print('B')
        exit()
print(nums[-1]*a + b)