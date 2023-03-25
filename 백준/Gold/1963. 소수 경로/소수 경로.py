from collections import deque
from sys import stdin
table = [False] * 10001
for i in range(2, int(10001**0.5) + 1):
    for j in range(i, 10001, i):
        table[j] = True
result = []
for idx, k in enumerate(table):
    if not k and idx > 1000:
        result.append(idx)

def bfs(r, x, y):
    queue = deque()
    queue.append((x,0))
    visit = [False] * 10001
    while queue:
        a, cnt = queue.popleft()
        if a == y:
            return cnt
        a = str(a)
        for i in range(4):
            for j in range(10):
                if a[i] != str(j):
                    na = a[:i] +str(j) + a[i+1:]
                    if int(na) in r and not visit[int(na)]:
                        visit[int(na)] = True
                        queue.append((int(na), cnt + 1))
t = int(stdin.readline())
for _ in range(t):
    a, b = map(int, stdin.readline().split())
    if a == b:
        print(0)
        continue
    check = bfs(result, a, b)
    print(check if check else 'Impossible')