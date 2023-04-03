import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
po = [0] + list(map(int, input().split()))
graph = [[i] for i in range(n+1)]
for i in range(1, n+1):
    lst = list(map(int, input().split()))
    graph[i] += lst[1:]
# print(graph)

def dfs(s, v):
    # print('start_v', v)
    vv = []
    for i in v:
        vv.append(i)
    visit = [False] * (n+1)
    queue = []
    queue.append(s)
    while queue:
        x = queue.pop()
        for l in graph[x]:
            if l in v and not visit[l]:
                visit[l] = True
                queue.append(l)
                vv.remove(l)
    # print('end_vv', vv)
    if not vv:
        return 1
    return 0

answer = float('inf')
for i in range(1, n):
    for j in combinations(list(range(1,n+1)), i):
        check_1 = []
        check_1_val = 0
        check_2 = []
        check_2_val = 0
        for ele in range(1, n+1):
            if ele in j:
                check_1.append(ele)
                check_1_val += po[ele]
            else:
                check_2.append(ele)
                check_2_val += po[ele]
        # print('check', check_1, check_2)
        if dfs(check_1[0], check_1) and dfs(check_2[0], check_2):
            if answer > abs(check_1_val - check_2_val):
                answer = abs(check_1_val - check_2_val)
                # print('answer', answer)
if answer == float('inf'):
    print(-1)
else:
    print(answer)