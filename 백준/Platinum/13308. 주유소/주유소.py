import sys, heapq
input = sys.stdin.readline
n, m = map(int, input().split())
price = [0] + list(map(int, input().split()))
graph = {i : dict() for i in range(1, n+1)}

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a][b] = w
    graph[b][a] = w
# print(graph)

def dijkstra(graph, start):
    distances = [[float('inf')] * 3 for _ in range(n + 1)]
    distances[start][0] = 0 # 거리
    for idx, i in enumerate(price):
        distances[idx][1] = i # 주유소 가격
    queue = []
    distances[start][2] = 0
    heapq.heappush(queue, (distances[start][0], distances[start][1], distances[start][2], start))
    
    while queue:
        now_dist, now_price, total, now = heapq.heappop(queue)
        
        if distances[now][0] < now_dist:
            continue
        
        for nxt, nxt_dist in graph[now].items():
            dist = now_dist + nxt_dist
            if distances[nxt][0] > dist:
                distances[nxt][0] = dist
                nxt_total = total + nxt_dist * now_price
                distances[nxt][2] = nxt_total
                if distances[nxt][1] > now_price:
                    distances[nxt][1] = now_price
                heapq.heappush(queue, (distances[nxt][0], distances[nxt][1], distances[nxt][2], nxt))
        # print(queue)
    return distances

result = dijkstra(graph, 1)
print(result[n][2])