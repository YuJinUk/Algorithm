from collections import deque
def solution(q1, q2):
    q1 = deque(q1)
    q2 = deque(q2)
    q1_sum = sum(q1)
    q2_sum = sum(q2)
    divid_2 = (q1_sum + q2_sum)//2
    l = len(q1)
    if q1_sum == q2_sum == divid_2:
        return 0
    cnt = 0
    while q1_sum != divid_2:
        if q1_sum > q2_sum:
            r = q1.popleft()
            q2.append(r)
            q1_sum -= r
            q2_sum += r
            cnt += 1
        elif q1_sum < q2_sum:
            r = q2.popleft()
            q1.append(r)
            q1_sum += r
            q2_sum -= r
            cnt += 1
        if cnt > (l * 10) :
            return -1
    return cnt