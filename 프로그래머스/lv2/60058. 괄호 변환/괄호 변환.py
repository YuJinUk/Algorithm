from collections import deque
import sys
sys.setrecursionlimit(100000)

def checking(p):
    left, right = 0, 0
    for i in p:
        if i == ")":
            right += 1
        else:
            left += 1
        if left < right:
            return False
    else:
        return True
    
def g(u, v):
    result = "("; result += v; result += ")"
    if len(u) >= 4: u = ''.join([")" if i == "(" else "(" for i in u[1:len(u)-1]])
    else: u = ""
    return result + u
    
def f(p):
    if p == "":
        return ""
    u, v = "", ""
    stack = deque()
    p = deque(p)
    while p:
        np = p.popleft()
        stack.append(np)
        if stack.count("(") == stack.count(")"):
            break
    u += "".join(stack)
    v += "".join(p)
    check = checking(u)
    if check:
        return u + f(v)
    else:
        return g(u, f(v))
def solution(p):
    return f(p)