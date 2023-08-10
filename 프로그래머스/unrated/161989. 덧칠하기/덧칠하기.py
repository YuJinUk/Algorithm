def solution(n, m, section):
    check = [1 for _ in range(n+1)]
    for i in section:
        check[i] = 0
    idx = section[0]
    answer = 0
    while idx <= section[-1]:
        if check[idx]:
            idx += 1
            continue
        check[idx : idx + m] = [1] * m
        answer += 1
    return answer