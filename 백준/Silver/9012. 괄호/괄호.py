# 9012 괄호
import sys
from collections import deque
t = int(sys.stdin.readline())
for _ in range(t):
    stack = deque()
    parenthesis = list(sys.stdin.readline())
    for i in parenthesis:
        if i == '(':
            stack.append(i)
        elif i == ')' :
            if not stack:
                stack.append(i)
                break
            elif stack[-1] == '(':
                stack.pop()
    if not stack:
        print('YES')
    else:
        print('NO')