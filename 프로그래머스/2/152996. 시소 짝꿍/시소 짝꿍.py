#def ls(a,b): # 최대 공약수 구하는 func
#    min_num = min(a,b)
#    li = []
#    for i in range(1,min_num+1):
#        if a%i == 0:
#            if b%i == 0:
#                li.append(i)
#    return li[-1]
#def solution(weights): #최소공배수 = a * b / 최대공약수임을 이용해볼 예정
#    result = 0
#    for i in range(len(weights)-1):
#        f = weights[i]
#        for j in range(i+1,len(weights)):
#            s = weights[j]
#            if f == s:
#                result += 1
#                continue
#            elif f == s*2 or f == s//2:
#                result += 1
#                continue
#            elif f*2 == s*3 or f*3 == s*2:
#                result += 1
#                continue
#            elif f*4 == s*3 or f*3 == s*4:
#                result += 1
#                continue
#            gcd = ls(f,s)
#            if f//gcd in [2,3,4] and s//gcd in [2,3,4]:
#                result += 1
from collections import Counter
def solution(weights): #최소공배수 = a * b / 최대공약수임을 이용해볼 예정
    result = 0
    nums = Counter(weights)
    key = list(nums.keys())
    value = list(nums.values())
    plus = 0
    
    for i in value: # 같은 무게를 가진 사람끼리의 조합 수
        if i != 1:
            plus += i * (i-1) //2

    for i in range(len(key)-1): # 다른 몸무게를 가진 사람과의 조합 수
        f = key[i]
        fv = value[i]
        for j in range(i+1,len(key)):
            s = key[j]
            sv = value[j]
            if f == s*2 or f*2 == s:
                result += fv * sv
                continue
            elif f*2 == s*3 or f*3 == s*2:
                result += fv * sv
                continue
            elif f*4 == s*3 or f*3 == s*4:
                result += fv * sv
                continue
    return result + plus