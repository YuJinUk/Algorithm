import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
bus = [list(map(int, input().split())) for _ in range(m)]

floyd = [[float('inf')]*(n+1) for _ in range(n+1)]

for i, j, val in bus:
    if floyd[i][j] > val:
        floyd[i][j] = val
        
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            floyd[i][j] = min(floyd[i][j], floyd[i][k] + floyd[k][j])
            
for i in range(1, n+1):
    floyd[i][i] = 0
    for idx, j in enumerate(floyd[i]):
        if j == float('inf'):
            floyd[i][idx] = 0
            
for i in range(1, n+1):
    print(*floyd[i][1:])