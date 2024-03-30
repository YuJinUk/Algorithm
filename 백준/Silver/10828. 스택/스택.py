import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

stack = deque()
def ppset(x, y=None):
    if x == "push":
        stack.append(y)
    elif x == "pop":
        if not stack:
            print(-1)
            return
        print(stack.pop())
    elif x == "size":
        print(len(stack))
    elif x == "empty":
        if stack:
            print(0)
        else:
            print(1)
    else:
        if not stack:
            print(-1)
            return
        print(stack[-1])
    return

for _ in range(N):
    ip = input().rstrip()
    if ip[:3] == "pus":
        a, b = ip.split()
        b = int(b)
    else:
        a = ip
        b = None
    ppset(a, b)