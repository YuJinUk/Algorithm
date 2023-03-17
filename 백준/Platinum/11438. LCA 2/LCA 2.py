from sys import stdin, setrecursionlimit
from math import log2
setrecursionlimit(int(1e6))

n = int(stdin.readline())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    parent, child = map(int, stdin.readline().split())
    tree[parent].append(child)
    tree[child].append(parent)

l = int(log2(1e5)) + 1
table = [[0]*l for _ in range(n+1)]
depth = [0]*(n+1)
visit = [False]*(n+1)

# node의 depth를 저장 및 table의 i번째 2^0위치를 부모로 갱신한다.
def dfs(node , deep):
    visit[node] = True
    depth[node] = deep

    for i in tree[node]:
        if not visit[i]:
            table[i][0] = node
            dfs(i, deep+1)

# 희소 배열 : 부모노드에 자식노드의 값을 2^n 에 비례하여 저장한다. (17435번에 table 생성하는 과정에 대해 자세히 적어둠)
def sparse():
    dfs(1,0) # root node : 1
    for i in range(1, l):
        for j in range(1, n+1):
            table[j][i] = table[table[j][i-1]][i-1]

def lca(x, y):
    # print(table)
    # x의 depth를 더 작게 설정
    if depth[x] > depth[y]:
        x, y = y, x

    # 깊이가 동일하게 맞출때 2^i 만큼 이동해준다. -> table[y][i]의 의미
    for i in range(l-1 , -1 , -1):
        if depth[y]-depth[x] >= (1<<i):
            y = table[y][i]
    # print(x, y)
    # 만약 깊이를 맞췄을 때 x와 y가 같으면 x가 y의 lca임으로 return x
    if x == y:
        return x
    # depth가 같지만 x랑 y가 다를 경우 둘다 한칸씩 위로 올리면서 같아질때까지 체크한다.
    for i in range(l-1,-1,-1):
        if table[x][i] != table[y][i]: # 두 부모가 다르다면 depth를 한칸씩 올림
            x = table[x][i]
            y = table[y][i]
        
    return table[x][0]

sparse()

m = int(stdin.readline())

for i in range(m):
    a, b = map(int,stdin.readline().split())
    print(lca(a, b))
