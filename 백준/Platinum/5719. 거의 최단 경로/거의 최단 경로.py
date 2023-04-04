import sys, heapq
from collections import deque
input = sys.stdin.readline
while True:
    n, m = map(int, input().split()) # n : node / m : edge
    if n == 0 and m == 0:
        break
    s, d = map(int, input().split()) # start, end
    graph = {i : dict() for i in range(n)}
    reverse_graph = {i : dict() for i in range(n)}
    for _ in range(m):
        u, v, p = map(int, input().split())
        graph[u][v] = p
        reverse_graph[v][u] = p
    # print('default graph',graph)
    # print('default reverse_graph',reverse_graph)
    def dijkstra(graph, start):
        check = []
        distances = [float('inf') for _ in range(n + 1)]
        distances[start] = 0
        queue = []
        heapq.heappush(queue, (0, [start]))
        
        while queue:
            now_dist, now = heapq.heappop(queue)
            if distances[now[-1]] < now_dist:
                continue
            for nxt, nxt_dist in graph[now[-1]].items():                
                dist = now_dist + nxt_dist
                if distances[nxt] > dist:
                    distances[nxt] = dist
                    heapq.heappush(queue, (dist, now + [nxt]))
        return distances[d]
                    # print((dist, now + [nxt]))
                # if nxt == d and check:
                #     print(check)
                #     a = heapq.heappop(check)
                #     if a[0] > dist:
                #         check = []
                #         heapq.heappush(check,(dist, now + [nxt]))
                #         continue
                #     elif a[0] == dist:
                #         heapq.heappush(check,(dist, now + [nxt]))
                #     heapq.heappush(check, a)
                # elif nxt == d and not check:
                #     heapq.heappush(check,(dist, now + [nxt]))
        # return distances, check

    def nxt_dijkstra(graph, start):
        distances = [float('inf') for _ in range(n + 1)]
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

    distance = nxt_dijkstra(graph, s)
    # print(distance)
    min_len = distance[d]
    queue = deque()
    queue.append((d, min_len))
    check = []
    while queue:
        now, mm = queue.popleft()
        if now == s:
            continue
        for nxt, nxt_val in reverse_graph[now].items():
            if distance[nxt] + nxt_val == mm:
                if (nxt, now) not in check:
                    # print('queue', queue)
                    queue.append((nxt, mm - nxt_val))
                    check.append((nxt, now))
        
    # print('check',check)
    for i in check:
        graph[i[0]].pop(i[1])
    # print(graph)
    answer = nxt_dijkstra(graph, s)
    # print(answer)
    print(answer[d] if answer[d] != float('inf') else -1)
    # distance, check = dijkstra(graph, s)
    # print(distance)
    # print(check)
    # if not check:
    #     print(-1)
    #     continue
    # a = set()
    # for i in check:
    #     for j in range(len(i[1])-1):
    #         a.add((i[1][j], i[1][j+1]))
    # print('aaaa',a)
    # for i in a:
    #     graph[i[0]].pop(i[1])
    # print(graph)
    # answer = nxt_dijkstra(graph, s)
    # print(answer)
    # print(answer[d] if answer[d] != float('inf') else -1)