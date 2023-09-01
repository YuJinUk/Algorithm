from collections import defaultdict

def sosu(x):
    for i in range(2, int(x**0.5) + 1):
        if not x % i:
            return 1 # 소수가 아님
    return 0 # 소수

def cnt_f(i, x):
    dic = {}
    dic[x] = 0
    while x > 1:
        mok, mod = divmod(i, x)
        if mod:
            break
        elif not mod:
            dic[x] += 1
            i = mok
    return x, dic[x]

N = int(input())
answer = defaultdict(int)
for x in range(2, N + 1):
    if not sosu(x):
        answer[x]
        for i in range(x, N + 1, x):
            a, b = cnt_f(i, x)
            answer[a] += b
            
answer = list(answer.values())
finish = 1
for i in answer:
    finish *= i*2 + 1
print(finish)