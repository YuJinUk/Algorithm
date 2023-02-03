from collections import deque
n, k = map(int, input().split()) # n : 온도를 측정한 전체 날짜 수 / k : 연속된 날짜 수
num = list(map(int, input().split()))
num = deque(num)
result = deque()

if n == k:
    print(sum(num))
elif len(set(num)) == 1:
    print(num[0]*k)
else:
    sum_num = 0
    max_num = 0

    while True:

        nums = num.popleft()

        if len(result) < k:
            result.append(nums)
            sum_num += nums
            max_num += nums

        else:
            va = result.popleft()
            if max_num < sum_num - va + nums:
                max_num = sum_num -va +nums
            sum_num = sum_num -va + nums
            result.append(nums)

        if not num:
            break

    print(max_num)