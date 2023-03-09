n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for idx in range(1,n+1):
    check = list(map(int, input().split()))
    for i in range(1,check[0]+1):
        graph[idx].append(check[i])

def bi(k):
    if visited[k]:
        return False
    visited[k] = True

    for num in graph[k]:
        if selected[num] == -1 or bi(selected[num]):
            selected[num] = k
            return True
    return False

selected = [-1] * (m+1)

for i in range(1,n+1):
    visited = [False] * (n+1)
    bi(i)
result = 0
for i in range(1, m+1):
    if selected[i] > -1:
        result += 1
print(result)