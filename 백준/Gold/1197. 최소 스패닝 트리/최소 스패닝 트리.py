def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

from sys import stdin
v, e = map(int, stdin.readline().split())
parent = [i for i in range(v+1)]
answer = 0
node = [tuple(map(int, stdin.readline().split())) for _ in range(e)]
node.sort(key = lambda x: x[2])
for a, b, c in node:
    if find(a) != find(b):
        union(a, b)
        answer += c
print(answer)