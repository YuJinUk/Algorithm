import heapq
import sys
V, E = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
node = {i:[] for i in range(1, V+1)}
for i in range(1, E+1):
    u, v, w = map(int, sys.stdin.readline().split())
    node[u].append((v,w))

def dijkstra(graph, start):
    dic_distance[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])
    while queue:
        now_dist, now_lo = heapq.heappop(queue)

        if dic_distance[now_lo] < now_dist:
            continue

        for new_lo, new_dist in graph[now_lo]:
            dist = now_dist + new_dist
            if dist < dic_distance[new_lo]:
                dic_distance[new_lo] = dist
                heapq.heappush(queue, [dist, new_lo])
    return dic_distance

dic_distance = [float('inf')] * (V+1)
result = dijkstra(node, k)
for i in range(1, V+1):
    if result[i] == float('inf'):
        print('INF')
    else:
        print(result[i])