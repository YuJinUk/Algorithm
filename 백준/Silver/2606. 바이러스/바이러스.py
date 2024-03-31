import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    if e in graph[s]:
        continue
    else: graph[s].append(e)
    if s in graph[e]:
        continue
    else: graph[e].append(s)

visited = [False] * (N + 1)
visited[1] = True
queue = deque()
queue.append(1)
while queue:
    x = queue.popleft()
    for nxt in graph[x]:
        if visited[nxt]:
            continue
        visited[nxt] = True
        queue.append(nxt)
print(sum(visited) - 1)