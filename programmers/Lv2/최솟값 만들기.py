def solution(a,b):
    a = sorted(a)
    b = sorted(b, reverse=True)
    result = 0
    l = len(a)
    for i in range(l):
        result += a[i] * b[i]
    return result