from collections import deque

def solution(n, edge):
    visited = deque()
    dic = dict()
    for i in range(1,n+1):
        dic.setdefault(i, [])
    for x, y in edge:
        dic[x].append(y)
        dic[y].append(x)
    start = 1
    cnt = 0
    visited = deque()
    visited.append((start, cnt))
    result = [-1]*(n+1)
    while visited:
        v, cnt = visited.popleft()
        if result[v] == -1:
            visited.append((v, cnt))
            result[v] = cnt
            cnt += 1
            for i in dic[v]:
                visited.append((i, cnt))
                dic[i].remove(v)
            del dic[v]
    max_value = result.count(max(result))
    return max_value