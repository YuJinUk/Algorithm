from collections import deque
def solution(p,l): # p : priorities / l : location
    
    p = deque(p)    
    sort_list = deque([i for i in range(len(p))])
    cnt = 0

    while True:

        lp = len(p)
        pop_p = p.popleft()
        pop_list = sort_list.popleft()

        for i in p:
            if pop_p < i:
                p.append(pop_p)
                sort_list.append(pop_list)
                break
        
        if len(p) != lp:
            if pop_list == l:
                cnt += 1
                return cnt
            cnt += 1

        if len(p) == 0:
            break