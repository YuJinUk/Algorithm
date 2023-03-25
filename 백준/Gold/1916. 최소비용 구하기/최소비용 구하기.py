from sys import stdin
import heapq
n = int(stdin.readline())
m = int(stdin.readline())
graph = {i : dict() for i in range(1, n + 1)}

for _ in range(m):
    a, b, c = map(int, stdin.readline().rstrip().split())
    if b in graph[a]:
        if graph[a][b] > c:
            graph[a][b] = c
    else:
        graph[a][b] = c
# print(graph)

start, end = map(int, stdin.readline().split())

def dijkstra(graph, start):
    distances = [float('inf') for i in range(n + 1)]
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        now_val, now = heapq.heappop(queue)

        if now_val > distances[now]:
            continue

        for nxt, nxt_val in graph[now].items():
            dist = nxt_val + now_val
            if dist < distances[nxt]:
                distances[nxt] = dist
                heapq.heappush(queue, (dist, nxt))

    return distances

answer = dijkstra(graph, start)
print(answer[end])