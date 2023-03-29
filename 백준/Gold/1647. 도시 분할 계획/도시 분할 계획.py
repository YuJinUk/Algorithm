def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x
    

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(m)]
info.sort(key = lambda x: x[2])
parent = [i for i in range(n + 1)]
answer = 0
check = 0
for i, j, val in info:
    if find_parent(i) != find_parent(j):
        union(i, j)
        answer += val
        check = val
print(answer - check)