from itertools import combinations
from copy import deepcopy
def check(archer, lst, start):
    global d
    max_cnt = 0
    rm_list = []
    for i in archer:
        dist = []
        for j in range(len(lst)):
            x = j + 1 # 세로 길이
            for k in range(len(lst[0])):
                y = abs(i-k) # 가로 길이
                if lst[j][k] and x+y <= d:
                    dist.append((x+y, j, k))                    
        dist.sort(key = lambda x: (x[0],x[2]))
        if dist:
            rm_list.append(dist[0])
    for c, a, b in rm_list:
        if lst[a][b]:
            lst[a][b] = 0
            matrix[start-a][b] = 0
            max_cnt += 1
    return max_cnt

n, m, d = map(int, input().split())
matrix_ = [list(map(int, input().split())) for _ in range(n)]

def a(archer):
    answer = 0
    for i in range(n-1, -1, -1):
        chec = [matrix[k] for k in range(i, i-d, -1) if k >= 0]
        remov = check(archer, chec, i)
        answer += remov
    return answer

result = 0
for i in combinations([i for i in range(m)], 3):
    matrix = deepcopy(matrix_)
    c = a(i)
    if result < c:
        result = c
print(result)