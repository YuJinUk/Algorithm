import sys, heapq
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = {i : dict() for i in range(1, n+1)}

for _ in range(m):
    u, v, c = map(int, input().split())
    if u not in graph[v]:
        graph[v][u] = c
    else:
        if graph[v][u] > c:
            graph[v][u] = c
            
arrive_node = list(map(int, input().split()))

distances = [float('inf') for _ in range(n+1)]

for i in arrive_node:
    distances[i] = 0

def dijkstra(graph, start):
    queue = []
    heapq.heappush(queue, (0, start))
    
    while queue:
        now_dist, now = heapq.heappop(queue)
        
        if distances[now] < now_dist:
            continue
        
        for nxt, nxt_dist in graph[now].items():
            dist = now_dist + nxt_dist
            if distances[nxt] > dist:
                distances[nxt] = dist
                heapq.heappush(queue, (dist, nxt))
    return

for i in arrive_node:
    dijkstra(graph, i)

answer = max(distances[1:])
print(distances.index(answer))
print(answer)