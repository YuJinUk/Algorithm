def solution(n):
    dp, i = 1, 2
    while True:
        dp *= i
        if dp > n:
            return i - 1
        elif dp == n:
            return i
        i += 1