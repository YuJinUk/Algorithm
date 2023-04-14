import sys
input = sys.stdin.readline
n = int(input())
val = [list(map(int, input().split())) for _ in range(n)]
def dfs(r, v):
    if r == n:
        return 0

    if visited[v] != -1:
        return visited[v]

    check = float('inf')
    for i in range(n):
        if (v & (1 << i)):
            continue
        check = min(check, dfs(r + 1, (v | (1 << i))) + val[r][i])
    visited[v] = check
    return visited[v]

visited = [-1] * (1 << n)
print(dfs(0, 0))