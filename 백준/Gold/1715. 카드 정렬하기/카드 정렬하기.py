import heapq
from sys import stdin, exit
n = int(stdin.readline())
if n == 1:
    print(0)
    exit()
heap = []
for _ in range(n):
    heapq.heappush(heap, int(stdin.readline()))
dp = 0
while heap:
    if len(heap) == 1:
        break
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    dp += a+b
    heapq.heappush(heap, a+b)
print(dp)