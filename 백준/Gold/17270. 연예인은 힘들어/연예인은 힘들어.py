import sys
input = sys.stdin.readline

v, m = map(int, input().split())
node = [list(map(int, input().split())) for _ in range(m)]
ji, su = map(int, input().split())

ployd = [[float('inf')]*(v+1) for _ in range(v+1)]

for i, j, val in node:
    if ployd[i][j] > val:
        ployd[i][j] = val
    if ployd[j][i] > val:
        ployd[j][i] = val

for i in range(1, v+1):
    ployd[i][i] = 0

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            if ployd[i][j] > ployd[i][k] + ployd[k][j]:
                ployd[i][j] = ployd[i][k] + ployd[k][j]

# print(ployd)
j, s = ployd[ji], ployd[su]
# print(j)
# print(s)
check = []
for i in range(1, v+1):
    if i == ji or i == su:
        continue
    check.append((j[i] + s[i], j[i], s[i], i))
if not check:
    print(-1)
    exit()
check.sort(key = lambda x: (x[0], x[1], x[3]))
# print(check)
min_val = check[0][0]
min_dist = float('inf')
position = 0
for a, b, c, d in check:
    if a > min_val:
        break
    elif b > c:
        continue
    elif a == float('inf'):
        continue
    elif min_dist > b:
        min_dist = b
        position = d
    elif min_dist == b:
        if position > d:
            position = d
if not position:
    print(-1)
else:
    print(position)