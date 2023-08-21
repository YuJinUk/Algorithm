def f(b, num):
    dic = {}
    for i in range(10, 17):
        dic[i] = chr(i + 55)
    for i in range(0, 10):
        dic[i] = str(i)
    result = ""
    while num >= b:
        mok, mod = divmod(num, b)
        result = dic[mod] + result
        num = mok
    result = dic[num] + result
    return result

def solution(n, t, m, p):
    answer = ""
    l = t * m
    num = 0
    while len(answer) < t*m:
        answer += f(n, num)
        # print(answer)
        num += 1
    result = ""
    for i in range(0, len(answer), m):
        result += answer[i + p - 1]
        if len(result) == t:
            break
    return result