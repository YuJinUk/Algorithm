from collections import deque
from sys import stdin

def find_parent(x):
    queue = deque()
    queue.append(x)
    while True:
        try:
            nxt = node[x][0]
            queue.append(nxt)
            x = nxt
        except IndexError:
            return queue

T = int(stdin.readline())
for tt in range(1, T+1):
    n = int(stdin.readline())
    node = {i : [] for i in range(1, n+1)}
    for _ in range(n-1):
        parent, child = map(int, stdin.readline().split())
        node[child].append(parent)
    a, b = map(int, stdin.readline().split())
    q_a, q_b = find_parent(a), find_parent(b)
    if len(q_a) > len(q_b):
        for i in q_b:
            if i in q_a:
                print(i)
                break
    else:
        for i in q_a:
            if i in q_b:
                print(i)
                break