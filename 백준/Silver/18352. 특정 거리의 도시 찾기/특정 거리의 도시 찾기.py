import sys, heapq
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = {i : dict() for i in range(1, n+1)}
for _ in range(m):
    s, e = map(int, input().split())
    graph[s][e] = 1
    
def dijkstra(graph, start):
    distances = [float('inf')] * (n+1)
    distances[start] = 0
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
    
    return distances

result = dijkstra(graph, x)
check = 0
for idx, i in enumerate(result):
    if i == k:
        print(idx)
        check += 1
else:
    if not check:
        print(-1)