def solution(n, s):
    if s < n:
        return [-1]
    if n == s:
        return [1]*n
    summ = s - n * (s//n)
    return [s//n] * (n-summ) + [s//n+1] * summ