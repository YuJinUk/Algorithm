# 이분 매칭 17481 최애 정하기
n, m = map(int, input().split())
members = {input() : i for i in range(1, m+1)}
graph = [[] for _ in range(n+1)]
for idx in range(1,n+1):
    check = list(input().split())
    for i in range(1,int(check[0])+1):
        graph[idx].append(members[check[i]])

# print(members)
# print(graph)

def bi(k):
    if visited[k]:
        return 0
    visited[k] = True

    for num in graph[k]:
        if selected[num] == -1 or bi(selected[num]):
            selected[num] = k
            return 1
    return 0

selected = [-1] * (m+1)
result = 0
for i in range(1,n+1):
    visited = [False] * (n+1)
    result += bi(i)
# print(selected)
if result == n:
    print('YES')
else:
    print('NO')
    print(result)