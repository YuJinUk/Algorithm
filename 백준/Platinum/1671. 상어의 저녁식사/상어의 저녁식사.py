# 이분 매칭 1671 상어의 저녁식사
N = int(input())
shark = dict()
for i in range(1, N+1):
    shark[i] = list(map(int, input().split()))
    
select = [-1] * (N+1)

def dfs(s):
    if visit[s]:
        return 0
    visit[s] = 1
    for next_n in graph[s]:
        if select[next_n] == -1 or dfs(select[next_n]):
            select[next_n] = s
            return 1
    return 0

graph = [[] for _ in range(N+1)]
for i in range(1, N):
    for j in range(i+1, N+1):
        if shark[i] == shark[j]:
            graph[i].append(j)
        else:
            cnt_i, cnt_j = 0, 0
            for k in range(3):
                if shark[i][k] >= shark[j][k]:
                    cnt_i += 1
                if shark[j][k] >= shark[i][k]:
                    cnt_j += 1
            if cnt_i == 3:
                graph[i].append(j)
            elif cnt_j == 3:
                graph[j].append(i)

ans = N
for i in range(1,N+1):
    visit = [0] * (N+1)
    ans -= dfs(i)
    visit = [0] * (N+1)
    ans -= dfs(i)
    # print(ans)
# print(graph)
print(ans)
