def solution(n, times):
    times.sort() # binary search는 무조건 정렬되어 있어야함
    answer = 0
    left, right = times[0], times[0] * n # left : 최소 시간, right : 최대 시간
    
    while left <= right :
        mid = (left + right)//2 # 중간값
        p = 0 # 사람 수
        for t in times : # mid동안 검사하는 사람의 수
            p += mid//t
        if p >= n : # 만약 mid동안 검사한 사람 수가 n보다 많으면
            answer = mid # mid값이 최소시간이 될 수 있으므로 answer에 mid를 갱신하고
            right = mid - 1 # 최대 시간을 mid-1로 갱신
        elif p < n : # 만약 mid동안 검사한 사람 수가 n보다 적으면
            left = mid + 1 # 최소 시간을 mid + 1로 갱신
            
    return answer