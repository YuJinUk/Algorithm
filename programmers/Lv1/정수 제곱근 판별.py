def solution(n):
    answer = 0
    if n <=1000000:
        a = [(i+1)**2 for i in range(1,1000) if i*i == n]
        if len(a) == 0:
            answer = -1
        else:
            answer = a[0]
    elif 1000000< n <= 10000000000:
        a = [(i+1)**2 for i in range(1000, 100000) if i*i == n]
        if len(a) == 0:
            answer = -1
        else:
            answer = a[0]
    else:
        a = [(i+1)**2 for i in range(100000, 10000000) if i*i == n]
        if len(a) == 0:
            answer = -1
        else:
            answer = a[0]
    return answer