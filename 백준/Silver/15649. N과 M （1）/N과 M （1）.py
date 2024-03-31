import sys
from collections import deque
input = sys.stdin.readline

def dfs():
    if len(per) == M:
        print(*per)
        return
    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = True
        per.append(i)
        dfs()
        visited[i] = False
        per.pop()

N, M = map(int, input().split())
visited = [False] * (N + 1)
per = deque()

dfs()