import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

def dfs(s, visited):
    visited.add(s)
    checked[s] = 1
    for v in dic[s]:
        if v not in visited:
            dfs(v, visited.copy())
        else: # 사이클이 생기면 뽑는다.
            result.extend(list(visited))
            return

N = int(sys.stdin.readline().strip())
dic = defaultdict(list)
for i in range(1, N+1):
    v = int(sys.stdin.readline().strip())
    dic[v].append(i)

checked = [0 for _ in range(N+1)]
result = []
for i in range(1, N+1):
    if not checked[i]:
        dfs(i, set([]))

result.sort()
print(len(result)) 
for x in result:
    print(x)