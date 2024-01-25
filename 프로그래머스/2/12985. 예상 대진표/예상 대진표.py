import math
def solution(n,a,b):
    
    ans = 1
    if b-a == 1 and not (a & (a-1)):
        return math.log2(a) + 1
    elif a-b == 1 and not (b & (b-1)):
        return math.log2(b) + 1
    while abs(a - b) > 1:
        if a % 2 == 1: 
            a += 1
        if b % 2 == 1:
            b += 1
        a /= 2
        b /= 2
        ans += 1
    
    if min(a,b) % 2 == 0:
        ans += 1
    
    return ans
