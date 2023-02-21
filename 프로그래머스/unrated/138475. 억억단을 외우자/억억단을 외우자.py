# from collections import deque
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

    result = []
    # result = deque()
    # for k in range(min(starts), e+1):
    #     result.append((check[k],k))
    # result.sort(key = lambda x: -x[0])
    # result = sorted(result, key = lambda x: -x[0])
    
    # ans = []
    # ans = deque()
    # for start in starts:
    #     for div_cnt, div in result:
    #         if start <= div:
    #             ans.append(div)
    #             break
    # return ans
    max_num = 0
    for idx in range(e,0,-1):
        if check[idx] >= max_num:
            max_num = check[idx]
            check[idx] = idx
        else:
            check[idx] = check[idx+1]
    return [check[i] for i in starts]