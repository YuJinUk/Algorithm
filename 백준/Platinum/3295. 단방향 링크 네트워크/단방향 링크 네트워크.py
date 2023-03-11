# 이분 매칭 3295 단방향 링크 네트워크
T = int(input())
for tt in range(1,T+1):
    n, m = map(int, input().split())
    graph = {i:[] for i in range(n)}

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    select = [-1] * n

    def dfs(s):
        if visit[s]:
            return 0
        visit[s] = True
        for next_n in graph[s]:
            if select[next_n] == -1 or dfs(select[next_n]):
                select[next_n] = s
                return 1
        return 0

    ans = 0
    for i in range(n):
        visit = [False] * n
        ans += dfs(i)

    print(ans)