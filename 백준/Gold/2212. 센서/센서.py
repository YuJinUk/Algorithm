import heapq
n = int(input())
k = int(input())

if k >= n:
    print(0)
    exit()

sensor = list(map(int, input().split()))
heapq.heapify(sensor)

distance = []
stack = []
while sensor:
    p = heapq.heappop(sensor)
    if not stack:
        stack.append(p)
    else:
        prior = stack.pop()
        heapq.heappush(distance, prior-p)
        stack.append(p)

for _ in range(k-1):
    heapq.heappop(distance)

print(-sum(distance))