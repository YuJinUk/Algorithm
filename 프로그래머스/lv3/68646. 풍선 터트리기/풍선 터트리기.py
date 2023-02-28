def solution(a):
    idx = a.index(min(a))
    left, right = 0, len(a)-1
    if idx == right:
        answer = 1
    else:
        answer = 2
    min_left, min_right = a[left], a[right]
    while left<idx:
        left += 1
        if min_left > a[left]:
            min_left = a[left]
            answer += 1
    while idx+1<right:
        right -= 1
        if min_right > a[right]:
            min_right = a[right]
            answer += 1
    return answer