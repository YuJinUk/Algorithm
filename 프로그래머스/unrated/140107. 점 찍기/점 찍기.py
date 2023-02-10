def solution(k, d):
    l = d//k
    result = 0
    for i in range(l+1):
        result += int((d**2 - (i * k)**2)**0.5)//k + 1
    return result