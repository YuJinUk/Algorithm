from collections import deque
n, k = map(int, input().split())
queue = deque()
queue.append(n)
check = [0] * (int(1e5) + 1)
cnt = 0
while queue:
    x = queue.popleft()
    if x == k:
        t = check[x]
        cnt += 1
        continue
    for nxt in [x-1, x+1, x*2]:
        if -1 < nxt <= int(1e5) and (not check[nxt] or check[nxt] == check[x] + 1):
            check[nxt] = check[x] + 1
            queue.append(nxt)
print(t)
print(cnt)