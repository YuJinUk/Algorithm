from collections import deque
def solution(n, roads, sources, destination):
    node = dict()
    for i in range(1, n+1):
        node.setdefault(i,[])
    for r1, r2 in roads:
        node[r1].append(r2)
        node[r2].append(r1)
    answer = deque([-1]*len(sources))
    visit = [False]*(n+1)
    result = deque()
    cnt = 0
    result.append((destination,cnt))
    while result:
        v, cnt = result.popleft()
        if v in sources:
            answer[sources.index(v)] = cnt
        for i in node[v]:
            if not visit[i]:
                result.append((i, cnt+1))
                visit[i] = True
    if destination in sources:
        answer[sources.index(destination)] = 0
    return list(answer)