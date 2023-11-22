import sys
from collections import deque
input = sys.stdin.readline

nums = "".join([input().rstrip().replace(" ", "") for _ in range(3)])

dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
queue = deque()
start = nums.find("0")
queue.append((start, nums, 0))
visited = {nums : 0}
answer = -1

while queue:
    x, num, r = queue.popleft()
    if num == "123456780":
        answer = r
        break
    rx, ry = divmod(x, 3)
    nxt = list(num)
    for dx, dy in dxdy:
        nx, ny = rx + dx, ry + dy
        if -1 < nx < 3 and -1 < ny < 3:
            nxt[x], nxt[nx*3 + ny] = nxt[nx*3 + ny], nxt[x]
            check = "".join(nxt)
            if check not in visited:
                queue.append((nx*3 + ny, check, r + 1))
                visited[check] = r
            nxt[x], nxt[nx*3 + ny] = nxt[nx*3 + ny], nxt[x]

print(answer)