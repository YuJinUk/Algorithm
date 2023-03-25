from sys import stdin
from collections import deque
n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)
visit = [False] * n
check = 0
def dfs(start, depth):
    global check
    visit[start] = True
    if depth == 4:
        check = 1
        return
    for i in graph[start]:
        if not visit[i]:
            visit[i] = True
            dfs(i, depth + 1)
            visit[i] = False
    visit[start] = False
    return 0

for i in range(n):
    dfs(i, 0)
    if check:
        print(1)
        exit()
else:
    print(0)