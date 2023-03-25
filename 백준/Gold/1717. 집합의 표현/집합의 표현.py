import sys
sys.setrecursionlimit(10**6)
def find(x):
    if x != table[x]:
        table[x] = find(table[x])
    return table[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        table[y] = x
    else:
        table[x] = y

n, m = map(int, sys.stdin.readline().split())
table = [i for i in range(n+1)]
for _ in range(m):
    check, a, b = map(int, sys.stdin.readline().split())
    if not check:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')