def dfs(start,visit):
    if len(visit) == k:
        for num in visit:
            print(num)
        exit()
    for i in range(start+1,n+1):
        if not visited[i]:
            for num in visit:
                if num not in node[i]:
                    break
            else:
                visited[i] = True
                dfs(i,visit+[i])

from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

k, n, f = map(int, stdin.readline().split())
node = {i : [] for i in range(1, n+1)}
for _ in range(f):
    a, b = map(int, stdin.readline().split())
    node[a].append(b)
    node[b].append(a)

for i in range(1,n+1):
    visited = [False] * (n+1)
    visited[i] = True
    dfs(i,[i])

print(-1)