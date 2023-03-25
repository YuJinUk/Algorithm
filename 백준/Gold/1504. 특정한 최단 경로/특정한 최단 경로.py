from sys import stdin
import heapq
n, m = map(int, stdin.readline().split())
graph = {i : dict() for i in range(1, n + 1)}
for _ in range(m):
    a, b, c = map(int, stdin.readline().rstrip().split())
    if b in graph[a]:
        if graph[a][b] > c:
            graph[a][b] = c
    else:
        graph[a][b] = c
    if a in graph[b]:
        if graph[b][a] > c:
            graph[b][a] = c
    else:
        graph[b][a] = c
v1, v2 = map(int, stdin.readline().split())
# print(graph)
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

w1 = dijkstra(graph, 1)
w2 = dijkstra(graph, v1)
w3 = dijkstra(graph, v2)

answer = min(w1[v1] + w2[v2] + w3[n], w1[v2] + w3[v1] + w2[n])
print(answer if answer != float('inf') else -1)