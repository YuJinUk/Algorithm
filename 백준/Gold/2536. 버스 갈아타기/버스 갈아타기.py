from collections import deque
from sys import stdin
m, n = map(int, stdin.readline().split())
k = int(stdin.readline())
bus = deque()
for _ in range(k):
    b, x1, y1, x2, y2 = map(int, stdin.readline().split())
    bus.append((b, min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)))
sx, sy, dx, dy = map(int, stdin.readline().split())

rm_bus = [False] * (k+1)
for i in range(k):
    b, x1, y1, x2, y2 = bus[i]
    for j in range(k):
        if i == j:
            continue
        new_b, new_x1, new_y1, new_x2, new_y2 = bus[j]
        if x1 == x2 == new_x1 == new_x2:
            if new_y1 <= y1 <= y2 <= new_y2:
                rm_bus[b] = True
                break
        if y1 == y2 == new_y1 == new_y2:
            if new_x1 <= x1 <= x2 <= new_x2:
                rm_bus[b] = True
                break
# print(rm_bus)
p = [[] for _ in range(k + 1)]
for i in range(k):
    b, x1, y1, x2, y2 = bus[i]
    if rm_bus[b]:
        continue
    for j in range(k):
        if i == j:
            continue
        new_b, new_x1, new_y1, new_x2, new_y2 = bus[j]
        if rm_bus[new_b]:
            continue
        # 한 점에서 만나는 경우 (방향이 서로 다른 경우)
        if x1 <= new_x1 <= x2 and x1 <= new_x2 <= x2:
            if new_y1 <= y1 <= new_y2 and new_y1 <= y2 <= new_y2:
                p[b].append(new_b)
                p[new_b].append(b)
        # 한 점 혹은 겹치는 경우 (수평 방향)
        if y1 == y2 == new_y1 == new_y2:
            if not (x1 > new_x2 or x2 < new_x1):
                p[b].append(new_b)
                p[new_b].append(b)
        # 한 점 혹은 겹치는 경우 (수직 방향)
        if x1 == x2 == new_x1 == new_x2:
            if not (y1 > new_y2 or y2 < new_y1):
                p[b].append(new_b)
                p[new_b].append(b)
# print(p)
visit = [-1] * (k + 1)
queue = deque()
end_queue = deque()
for i in range(k):
    b, x1, y1, x2, y2 = bus[i]
    if rm_bus[b]:
        continue
    if x1 == sx and y1<= sy <= y2:
        queue.append(b)
        visit[b] = 1
    elif y1 == sy and x1<= sx <= x2:
        queue.append(b)
        visit[b] = 1
    if x1 == dx and y1<= dy <= y2:
        end_queue.append(b)
    elif y1 == dy and x1<= dx <= x2:
        end_queue.append(b)
# print(queue)
# print(end_queue)
while queue:
    # print(queue)
    bus_num = queue.popleft()
    for i in p[bus_num]:
        if visit[i] == -1:
            visit[i] = visit[bus_num] + 1
            queue.append(i)
# print(visit)
answer = float('inf')
for i in end_queue:
    answer = visit[i] if answer > visit[i] else answer
print(answer)