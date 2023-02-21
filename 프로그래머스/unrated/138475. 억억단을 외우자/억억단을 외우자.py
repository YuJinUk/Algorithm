def solution(e, starts):
    
    check = [1] * (e+1)
    for i in range(2, e + 1):
        for j in range(i, e + 1):
            if i * j > e:
                break
            if i == j:
                check[i*i] += 1
                continue
            check[i*j] += 2
    max_num = 0
    for idx in range(e,0,-1):
        if check[idx] >= max_num:
            max_num = check[idx]
            check[idx] = idx
        else:
            check[idx] = check[idx+1]
    return [check[i] for i in starts]