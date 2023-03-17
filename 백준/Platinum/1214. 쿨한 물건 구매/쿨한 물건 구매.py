def solution():
    d, p, q = map(int, input().split())

    if not d % p or not d % q:
        return d

    p, q = max(p, q), min(p, q) # p > q
    l = d // p + 1
    answer = p * l

    for i in range(l-1, -1, -1):
        # print('iii',i)
        mok, mod = divmod((d - (i * p)), q)
        # print(mok, mod)
        if not mod:
            return d
        check = (i * p) + ((mok + 1) * q) # i에 대한 최소값
        # print('check', check)
        if answer == check:
            break
        answer = check if check < answer else answer
    return answer

print(solution())