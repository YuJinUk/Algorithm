from itertools import combinations
from collections import deque
n, m = map(int, input().split())
dic = dict()
for i in range(1,n+1):
    dic.setdefault(i, [])

answer = deque([[0]*(n+1) for _ in range(n+1)])

for _ in range(m):
    parent, child = map(int, input().split())
    dic[parent].append(child)
    dic[child].append(parent)

for start in dic:
    visited = [False for _ in range(n+1)]
    dist = 0
    result = deque()
    result.append((start,dist))
    while result:
        v, dist = result.popleft()
        if not visited[v]:
            visited[v] = True
            for i in dic[v]:
                if not visited[i]:
                    result.append((i, dist+1))
                    answer[start][i] = dist+1
                    
combi = list(combinations(list(range(1, n+1)), 2))
checking_list = []

for c1, c2 in combi:
    cnt = 0
    for check1, check2 in zip(answer[c1], answer[c2]):
        cnt += check2 if check1 > check2 else check1
    checking_list.append([c1,c2,cnt*2])
checking_list.sort(key = lambda x: (x[2], x[0], x[1]))
print(*checking_list[0])