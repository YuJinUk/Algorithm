from collections import deque
n = int(input())
node = {i:[] for i in range(1,n+1)}
for _ in range(n-1):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

visit = [False] * (n+1)
v = deque()
v.append((1,0))
ans = 0
while v:
    x, cnt = v.pop()
    if x != 1 and len(node[x]) == 1:
        ans += cnt
        continue
    for i in node[x]:
        if not visit[i]:
            visit[i] = True
            v.append((i,cnt+1))

if ans % 2:
    print('Yes')
else:
    print('No')