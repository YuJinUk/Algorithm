def solution(numbers, n):
    m = n
    for i in numbers: 
        n -= i
        if n < 0: return m - n