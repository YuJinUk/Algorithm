import sys
k, n = map(int, sys.stdin.readline().split())
graph = [[1e9] * (k+1) for _ in range(k+1)]

graph[0][0] = 0
for i in range(1, k+1):
    graph[i][i-1] = 0
    graph[i][i] = 0
    graph[i-1][i] = 1

for _ in range(n):
    x, y, r = map(int, sys.stdin.readline().split())
    if graph[x-1][y] > r:
        graph[x-1][y] = r
    graph[y][x-1] = (-1) * r

for i in range(k+1):
    for j in range(k+1):
        for h in range(k+1):
            if graph[j][h] > graph[j][i] + graph[i][h]:
                graph[j][h] = graph[j][i] + graph[i][h]

for i in range(k):
    if graph[i][i] < 0:
        print('NONE')
        exit()

for i in range(1, k+1):
    if graph[0][i] - graph[0][i-1] == 1:
        print('#', end = '')
    else:
        print('-', end = '')
print()