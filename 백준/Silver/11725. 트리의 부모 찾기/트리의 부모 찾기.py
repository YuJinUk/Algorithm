n = int(input())
graph = [[] for _ in range(n+1)]
result = dict()
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    result[i+2] = []
visit = [False] * (n+1)
v = [1]
while v:
    s = v.pop()
    visit[s] = True
    for i in graph[s]:
        if not visit[i]:
            visit[i] = True
            v.append(i)
            result[i].append(s)
for i in result:
    print(result[i][0])