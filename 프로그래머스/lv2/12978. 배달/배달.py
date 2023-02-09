# 다익스트라(dijkstra) 알고리즘
import heapq

def solution(n,road,k):
    # roads = []
    # for i in road:
    #     a, b, c = i
    #     a, b = min(a, b), max(a, b)
    #     roads.append([a,b,c])
    # heapq.heapify(roads)
    roads = road
    visited = [float('inf')] * (n+1) # inf로 설정하여 더 작은값이 나올때마다 갱신
    graph = [[] for i in range(n+1)] # start에 맞는 index에 넣기 위해 n+1개의 2차원 list 생성
    
    for start, end, t in roads: # 출발하는 위치의 index에 도착지의 위치 및 weight를 넣기 위함
        graph[start].append((end, t))
        graph[end].append((start,t))
    
    # print(graph)
    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        visited[start] = 0

        while q:
            dist, now = heapq.heappop(q) # dist는 현재까지의 거리, now는 현재 위치한 node
            
            if visited[now] < dist: # 만약 dist가 기존보다 크면 더 이상 탐색할 필요가 없음
                continue

            for i in graph[now]: # 연결된 노드를 탐색 
                if dist + i[1] < visited[i[0]]: # 만약 기존에 입력되있는 값이 크면
                    visited[i[0]] = dist + i[1] # 더 작은 값으로 갱신
                    heapq.heappush(q, (dist+i[1],i[0])) # q에 추가

    dijkstra(1)
    # print(visited)
    cnt = 0
    for i in visited:
        if i <= k:
            cnt += 1
    return cnt