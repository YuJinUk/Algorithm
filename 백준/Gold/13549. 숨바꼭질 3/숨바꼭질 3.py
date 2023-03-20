from collections import deque
n, k = map(int, input().split())
queue = deque()
queue.append(n)
check = [-1] * (int(1e5) + 1)
check[n] = 0
while queue:
    x = queue.popleft()
    if x == k:
        print(check[x])
        break
    a = x
    while -1 < a*2 <= int(1e5) and check[a*2] == -1:
        check[a*2] = check[a]
        queue.append(a*2)
        a *= 2
    for nxt in [x-1, x+1]:
        if -1 < nxt <= int(1e5) and check[nxt] == -1:
            check[nxt] = check[x] + 1
            queue.append(nxt)