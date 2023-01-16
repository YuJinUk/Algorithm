def al(x):
    num = []
    for i in range(1,int(x**0.5)+1):
        if x%i == 0:
            num.append(i)
            if i**2 != x:
                num.append(x//i)
    return num
def solution(n):
    li = al(n)
    result = 0
    for i in li:
        if i % 2 ==1:
            result +=1
    return result