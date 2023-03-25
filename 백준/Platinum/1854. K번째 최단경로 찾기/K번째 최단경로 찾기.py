from sys import stdin
import heapq
n, m, k = map(int, stdin.readline().split())
graph = {i : dict() for i in range(1, n + 1)}

for _ in range(m):
    a, b, c = map(int, stdin.readline().rstrip().split())
    if b in graph[a]:
        if graph[a][b] > c:
            graph[a][b] = c
    else:
        graph[a][b] = c
# print(graph)

def dijkstra(graph, start):
    distances = [[float('inf')] * k for _ in range(n + 1)]
    distances[start][0] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        now_val, now = heapq.heappop(queue)
        for nxt, nxt_val in graph[now].items():
            dist = nxt_val + now_val
            if dist < distances[nxt][k-1]:
                heapq.heappush(queue, (dist, nxt))
                distances[nxt][k-1] = dist
                distances[nxt].sort()
    return distances

d = dijkstra(graph, 1)
for i in range(1, n+1):
    if d[i][k-1] == float('inf'):
        print(-1)
    else:
        print(d[i][k-1])