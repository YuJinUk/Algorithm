import sys

input = sys.stdin.readline

N, M, V = map(int, input().split())

def dfs(s, graph, visit):
    if visit[s]:
        return
    visit[s] = True
    print(s, end=' ')
    for nxt in graph[s]:
        dfs(nxt, graph, visit)

def bfs(s, graph, visit):
    queue = [s]
    visit[s] = True
    while queue:
        current = queue.pop(0)
        print(current, end=' ')
        for nxt in graph[current]:
            if not visit[nxt]:
                visit[nxt] = True
                queue.append(nxt)

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1, N + 1):
    graph[i].sort()

visit_dfs = [False] * (N + 1)
dfs(V, graph, visit_dfs)
print()

visit_bfs = [False] * (N + 1)
bfs(V, graph, visit_bfs)
print()