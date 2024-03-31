import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip())
sortlist = []
for _ in range(N):
    heapq.heappush(sortlist, int(input().rstrip()))
for _ in range(len(sortlist)):
    print(heapq.heappop(sortlist))