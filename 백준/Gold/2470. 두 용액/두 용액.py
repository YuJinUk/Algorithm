import heapq
from sys import stdin
n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
answer = []
heap = []
for i in nums:
    heapq.heappush(heap, (abs(i),i))
answer.append(heapq.heappop(heap)[1])
result = float('inf')
for _ in range(len(heap)):
    a, b = heapq.heappop(heap)
    check = answer[-1] + b
    if result > abs(check):
        result = abs(check)
        m = [answer[-1], b]
    answer.pop()
    answer.append(b)
print(*sorted(m))