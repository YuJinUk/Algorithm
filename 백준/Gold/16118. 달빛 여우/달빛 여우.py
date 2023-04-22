import sys, heapq
input = sys.stdin.readline

# n, m = 5, 6
# a = [[1,2,3],[1,3,2],[2,3,2],[2,4,4],[3,5,4],[4,5,3]]
n, m = map(int, input().split())
graph = {i : dict() for i in range(1, n+1)}
for i in range(m):
    start, end, weight = map(int, input().split())
#    start, end, weight = a[i]
    graph[start][end] = weight
    graph[end][start] = weight
#print(graph)

def dijkstra_1(graph, start):
    distances = [float('inf') for _ in range(n+1)]
    queue = []
    distances[start] = 0
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

def dijkstra_2(graph, start):
    distances = [[float('inf')]*2 for _ in range(n+1)]
    queue = []
    distances[start][0] = 0
    cnt = 0
    heapq.heappush(queue, (0, start, cnt))
    
    while queue:
        now_dist, now, cnt = heapq.heappop(queue)
        
        if not cnt%2 and distances[now][0] < now_dist:
            continue
        elif cnt%2 and distances[now][1] < now_dist:
            continue
            
        for nxt, nxt_dist in graph[now].items():
            if not cnt%2:
                dist = now_dist + nxt_dist/2
                if distances[nxt][1] > dist:
                    distances[nxt][1] = dist
                    heapq.heappush(queue, (dist, nxt, cnt+1))
            else:
                dist = now_dist + nxt_dist*2
                if distances[nxt][0] > dist:
                    distances[nxt][0] = dist
                    heapq.heappush(queue, (dist, nxt, cnt+1))
    return distances

fox = dijkstra_1(graph, 1)
wolf = dijkstra_2(graph, 1)
# print(fox)
# print(wolf)
answer = 0
for i in range(2, n+1):
    if fox[i] < min(wolf[i]):
        answer += 1
print(answer)