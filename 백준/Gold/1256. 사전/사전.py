from math import factorial as fac
def f():
    m, n, k = map(int, input().split())
    if fac(m+n) // (fac(m)*fac(n)) < k:
        return -1
    a, b, c = m, n, k
    answer = ''
    z_cnt = n-1
    a_cnt = 0
    while True:
        while True:
            if z_cnt < 0:
                answer += 'a' * m
                return answer
            alpha = fac(z_cnt+a_cnt) // (fac(z_cnt) * fac(a_cnt))
            if alpha < k:
                k -= alpha
                a_cnt += 1
            else:
                break
        answer += 'a' * (m-a_cnt) + 'z'
        m = a_cnt
        z_cnt -=1
        a_cnt = 0
        if k == 0:
            break
        if len(answer) == a+b:
            break
    return answer
print(f())