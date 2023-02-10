from collections import deque
def solution(x, y, n):
    result = deque()
    result.append((y,0))
    while result:
        y, cnt = result.popleft()
        if y == x:
            return cnt
        if y % 2 == 0 and y//2 >= x:
            result.append((y // 2, cnt + 1))
        if y % 3 == 0 and y//3 >= x:
            result.append((y // 3, cnt + 1))
        if y - n >= x:
            result.append((y-n, cnt + 1))
    return -1
            