from collections import deque
def solution(p, s): # p : progresses / s : speeds
    p = deque(p)
    s = deque(s)
    result = deque()
    while True:
        cnt = 0
        if len(p) == 0:
            break
        
        p = deque([i+j for i,j in zip(p,s)])

        while p[0] >= 100:
            p.popleft()
            s.popleft()
            cnt += 1
            if len(p) == 0:
                result.append(cnt)
                break
            elif p[0] < 100:
                result.append(cnt)
    
    return list(result)