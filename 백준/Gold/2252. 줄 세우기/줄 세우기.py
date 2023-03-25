from collections import deque
from sys import stdin
n, m = map(int, stdin.readline().split())
graph_p = [[] for _ in range(n+1)]
graph_c = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph_p[a].append(b)
    graph_c[b].append(a)
# print(graph_p)
# print(graph_c)
visited = [False] * (n+1)
queue = deque()
answer = deque()
for idx, i in enumerate(graph_c):
    if not i:
        queue.append(idx)
        visited[idx] = True
        answer.append(idx)
answer.popleft()
queue.popleft()
# print(queue)
while queue:
    now = queue.popleft()
    for nxt in graph_p[now]:
        graph_c[nxt].remove(now)
        if not visited[nxt] and not len(graph_c[nxt]):
            visited[nxt] = True
            queue.append(nxt)
            answer.append(nxt)
print(*answer)