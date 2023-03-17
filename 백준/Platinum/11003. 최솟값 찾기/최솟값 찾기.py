from collections import deque
from sys import stdin
n, l = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))

queue = deque()
answer = deque()
for i in range(n):
    while queue and queue[-1][0] > nums[i]:
        queue.pop()
    while queue and queue[0][1] < i - l + 1:
        queue.popleft()
    queue.append((nums[i],i))
    answer.append(queue[0][0])
print(*answer)