from collections import deque
n, k = map(int, input().split())
cnt = 0
queue = deque()
queue.append(n)
check = [0] *(int(1e5) + 1)
while queue:
    x = queue.popleft()
    if x == k:
        print(check[x])
        break
    for nxt in [x-1, x+1, x*2]:
        if -1 < nxt <= int(1e5) and not check[nxt]:
            check[nxt] = check[x] + 1
            queue.append(nxt)