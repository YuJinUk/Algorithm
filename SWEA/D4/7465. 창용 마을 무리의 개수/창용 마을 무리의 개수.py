def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

T = int(input())
for tt in range(1, T+1):
    v, e = map(int, input().split())
    parent = [0] * (v + 1)
    
    for i in range(1, v + 1):
        parent[i] = i

    edge = []
    for i in range(e):
        a, b = map(int, input().split())
        union(a, b)
        edge.append([a,b])
    
    for x, y in edge:
        union(x, y)
    print(f'#{tt} {len(set(parent))-1}')