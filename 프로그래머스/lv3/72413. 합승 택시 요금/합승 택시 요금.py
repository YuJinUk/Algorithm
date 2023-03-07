#다익스트라
import heapq

def solution(n,s,a,b,fares):
    dic = dict()
    for i in range(1, n+1):
        dic[i] = dict()
        
    for i, j, k in fares:
        dic[i][j] = k
        dic[j][i] = k
    
    def dijkstra(graph, start):
        dic_distance[start] = 0
        queue = []
        heapq.heappush(queue, [start, 0])
        while queue:
            now_lo, now_dist = heapq.heappop(queue)

            if dic_distance[now_lo] < now_dist:
                continue

            for new_lo, new_dist in graph[now_lo].items():
                dist = now_dist + new_dist
                if dist < dic_distance[new_lo]:
                    dic_distance[new_lo] = dist
                    heapq.heappush(queue, [new_lo, dist])
        return dic_distance
    
    dic_distance = {alpha : float('inf') for alpha in range(1, n+1)}
    d = dijkstra(dic, s)
    m = float('inf')
    for i in range(1, n+1):
        dic_distance = {beta : float('inf') for beta in range(1, n+1)}
        d1 = dijkstra(dic, i)
        check = d1[a] + d1[b] + d[i]
        if m > check:
            m = check
    return m

#플로이드 워샬
# def solution(n, s, a, b, fares):
#     answer = float('inf')
    
#     dic = dict()
#     for i in range(1, n+1):
#         dic[i] = dict()
#         for j in range(1, n+1):
#             dic[i][j] = float('inf')
#         dic[i][i] = 0
        
#     for i, j, k in fares:
#         dic[i][j] = k
#         dic[j][i] = k
    
#     for k in range(1,n+1):
#         for i in range(1,n+1):
#             for j in range(1,n+1):
#                 dic[i][j] = min(dic[i][j], dic[i][k] + dic[k][j])
    
#     answer = float('inf')
#     for i in range(1,n+1):
#         dist = dic[s][i] + dic[i][a] + dic[i][b]
#         if answer > dist:
#             answer = dist
#     return answer