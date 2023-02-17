from itertools import combinations
def solution(clo):
    answer = 1
    type =[]
    for i in range(len(clo)):
        type.append(clo[i][1])
    type = sorted(type)
    li = [i+1 for i in range(len(type)-1) if type[i] != type[i+1]]+[len(type)]
    zz = [li[0]]
    for i in range(len(li)-1):
        zz.append(li[i+1]-li[i])
    for i in range(len(zz)):
        answer = answer *(1+zz[i])
        
    return answer-1