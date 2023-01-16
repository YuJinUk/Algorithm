def solution(n):
    n_2 = bin(n)
    get_1 = n_2.count('1')
    i = 1
    while True:
        get_2 = bin(n+i).count('1')
        if get_1 == get_2:
            break
        i += 1
    return n+i