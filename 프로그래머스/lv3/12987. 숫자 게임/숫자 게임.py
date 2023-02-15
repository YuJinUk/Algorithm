from collections import deque
def solution(a, b):
    a.sort()
    b.sort()
    a = deque(a)
    b = deque(b)
    cnt = 0
    while a:
        a_a = a.popleft()
        result = cnt
        for _ in range(len(b)):
            b_b = b.popleft()
            if b_b > a_a:
                cnt += 1
                break
            else:
                b.append(b_b)
        if result == cnt:
            break
    return cnt