import sys
from collections import defaultdict

sys.setrecursionlimit(10**7)

input = sys.stdin.readline

N, M = map(int, input().split())

P = [i for i in range(N + 1)]

def find(x):
    if P[x] != x:
        P[x] = find(P[x])
    
    return P[x]

def union(x, y):
    a, b = find(x), find(y)
    if a != b:
        P[a] = b
        
for _ in range(M):
    x, y = map(int, input().split())
    if x > y:
        x, y = y, x
    if find(x) != find(y):
        union(x, y)

for i in range(1, N + 1):
    find(i)

P = set(P)

print(len(P)-1)