from math import gcd
def solution(a, b):
    if len(a) == 1:
        a_gcd = a[0]
    elif len(a)>=2:
        a_gcd = gcd(a[0],a[1])
        if a_gcd != 1:
            for i in range(2, len(a)):
                a_gcd = gcd(a_gcd, a[i])
    
    if len(b) == 1:
        b_gcd = b[0]
    elif len(b)>=2:
        b_gcd = gcd(b[0],b[1])
        if b_gcd != 1:
            for i in range(2, len(b)):
                b_gcd = gcd(b_gcd, b[i])

    num = []
    if a_gcd != 1:
        for i in b:
            if i % a_gcd !=0:
                continue
            else:
                break
        else:
            num.append(a_gcd)
    
    if b_gcd != 1:
        for i in a:
            if i % b_gcd !=0:
                continue
            else:
                break
        else:
            num.append(b_gcd)

    return max(num) if num else 0