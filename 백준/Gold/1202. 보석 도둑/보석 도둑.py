import heapq
n, m = map(int, input().split())
j = []
for _ in range(n):
    heapq.heappush(j, list(map(int, input().split())))
b = sorted([int(input()) for _ in range(m)])

result = []
ans = 0
for siz in b:
    while j and j[0][0] <= siz:
        heapq.heappush(result, -heapq.heappop(j)[1])
    if result:
        ans -= heapq.heappop(result)
    elif not j:
        break
print(ans)
