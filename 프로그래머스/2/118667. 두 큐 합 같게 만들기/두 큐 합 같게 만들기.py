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

    # q1_minus = divid_2 - q1_sum
    # q2_minus = divid_2 - q2_sum
    # result = deque()
    # if q1_minus > 0 and q1_minus in q2: # 만약 차이가 반대쪽에 있으면 인덱스만큼의 길이
    #     result.append(q2.index(q1_minus))
    # elif q2_minus > 0 and q2_minus in q1:
    #     result.append(q1.index(q2_minus))
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
    # result.append(cnt)
    # return min(result)
    return cnt