import sys
import heapq

input = sys.stdin.readline

N = int(input())

heap = []
for _ in range(N):
    s, e = map(int, input().split())
    heapq.heappush(heap, (s, e))

rooms = []
rooms.append(heapq.heappop(heap)[1])
for _ in range(N-1):
    x = heapq.heappop(heap)
    if rooms[0] <= x[0]:
        heapq.heappop(rooms)
    heapq.heappush(rooms, x[1])

print(len(rooms))