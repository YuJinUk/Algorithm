from collections import deque
def solution(routes):
    if len(routes) == 1:
        return 1
    routes.sort(key = lambda x: x[1])
    stack = deque()
    i = 0
    while i < len(routes):
        stack.append(routes[i])
        j = i+1
        while True:
            if j == len(routes):
                i = j
                break
            if routes[j][0] > stack[-1][1]:
                i = j
                break
            elif routes[j][0] <= stack[-1][1]:
                j += 1
            if j == len(routes):
                i = j
                break
    return len(stack)