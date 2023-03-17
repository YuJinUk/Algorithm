import heapq
from sys import stdin
n = int(stdin.readline())
heap = []
for i in range(1, n+1):
    age, name = stdin.readline().split()
    heapq.heappush(heap, (int(age), i, name))
for _ in range(n):
    age, idx, name = heapq.heappop(heap)
    print(age, name)