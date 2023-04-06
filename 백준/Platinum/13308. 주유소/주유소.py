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
    distances = [[float('inf')] * (max(price) + 1) for _ in range(n + 1)]
    # for i in distances:
    #     i['distance'] = float('inf')
    # distances[start]['distance'] = 0 # 거리
    distances[start][price[start]]
    queue = []
    heapq.heappush(queue, (0, price[start], start))
    
    while queue:
        now_fee, now_price, now = heapq.heappop(queue)
        
        if distances[now][now_price] < now_fee:
            continue
        if now == n:
            return now_fee
        for nxt, nxt_dist in graph[now].items():
            nxt_price = now_price if price[nxt] > now_price else price[nxt]
            nxt_fee = now_fee + nxt_dist * now_price
            if distances[nxt][now_price] > nxt_fee:
                distances[nxt][now_price] = nxt_fee
                heapq.heappush(queue, (nxt_fee, nxt_price, nxt))
        # print(queue)
    return distances

# result = dijkstra(graph, 1)
# print(min(result[-1]))
print(dijkstra(graph, 1))
