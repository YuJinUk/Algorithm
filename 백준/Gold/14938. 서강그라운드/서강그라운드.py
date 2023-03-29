import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
t = [0] + list(map(int, input().split()))
node = [list(map(int, input().split())) for _ in range(r)]

floyd = [[float('inf')]*(n+1) for _ in range(n+1)]

for i, j, val in node:
    if floyd[i][j] > val:
        floyd[i][j] = val
    if floyd[j][i] > val:
        floyd[j][i] = val

for i in range(1, n+1):
    floyd[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            floyd[i][j] = min(floyd[i][j], floyd[i][k] + floyd[k][j])

answer = 0
for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if floyd[i][j] <= m:
            cnt += t[j]
    if answer < cnt:
        answer = cnt
print(answer)