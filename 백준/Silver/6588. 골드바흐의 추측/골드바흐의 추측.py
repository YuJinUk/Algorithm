def sosu():
    check = [False] * 1000001
    check[1] = True
    for i in range(2, int(len(check)**0.5)+1):
        for j in range(i * 2, len(check), i):
            check[j] = True
    return check

s = sosu()

def f(x):
    for i in range(2, x-1):
        if not s[i] and not s[x-i]:
            return i, x-i
    else:
        return "Goldbach's conjecture is wrong."

import sys
input = sys.stdin.readline

while True:
    num = int(input())
    if not num :
        break
    answer = f(num)
    if len(answer) == 2:
        print('{} = {} + {}'.format(num, answer[0], answer[1]))
    else:
        print(answer)