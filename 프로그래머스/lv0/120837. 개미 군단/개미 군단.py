def solution(hp):
    answer = 0
    n, mok = divmod(hp,5)
    answer += n
    if mok:
        n, mok = divmod(mok, 3)
        answer += n
        if mok:
            answer += mok
    return answer