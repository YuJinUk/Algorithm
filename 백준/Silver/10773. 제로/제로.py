# 10773 제로
import sys
from collections import deque
k = int(sys.stdin.readline())
stack = deque()
for i in range(k):
    num = int(sys.stdin.readline())
    if num:
        stack.append(num)
    elif not num:
        stack.pop()
print(sum(stack))