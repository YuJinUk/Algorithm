import sys, heapq
input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    
    if n == 1:
        print(1)
        continue
    
    heapq.heapify(nums)
    answer = 1
    
    while len(nums)>1:
        x = heapq.heappop(nums)
        y = heapq.heappop(nums)
        check = x * y
        heapq.heappush(nums, check)
        answer *= check
    print(answer % (int(1e9) + 7))