def solution(n):
    result = [[] for _ in range(n)]
    i = 1
    idx = -1
    num = 1
    while n > 0:
        mok = i // 3
        if i % 3 == 1: # index += 1
            for k in range(num,num+n):
                idx += 1
                result[idx].insert(mok,k)
        elif i % 3 == 2: # index 고정
            a = mok
            for k in range(num,num+n):
                a += 1
                result[idx].insert(a,k)
                
        else: # index -= 1
            for k in range(num,num+n):
                idx -= 1
                result[idx].insert(mok,k)

        num += n
        i += 1
        n -= 1
    ans = []
    for j in result:
        ans += j
    return ans