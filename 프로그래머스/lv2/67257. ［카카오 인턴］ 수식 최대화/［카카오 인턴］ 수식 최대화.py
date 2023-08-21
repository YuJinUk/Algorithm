from itertools import permutations

def f(opers, t, result):
    if result.isdigit():
        return str(result)
    elif not opers:
        return str(eval(result))
    oper = opers[t-1]
    
    if oper == '+':
        nxts = result.split('+')
        mid = []
        for nxt in nxts:
            mid.append(f(opers, t + 1, nxt))
        return str(eval('+'.join(map(str, mid))))
    if oper == '-':
        nxts = result.split('-')
        mid = []
        for nxt in nxts:
            mid.append(f(opers, t + 1, nxt))
        return str(eval('-'.join(map(str,mid))))
    if oper == '*':
        nxts = result.split('*')
        mid = []
        for nxt in nxts:
            mid.append(f(opers, t + 1, nxt))
        return str(eval('*'.join(map(str,mid))))


def solution(expression):
    N = len(expression)
    opers = list(permutations(['*', '-', '+'], 3))
    answer = 0
    
    for oper in opers:
        result = abs(int(f(list(oper), 1, expression)))
        if answer < result:
            answer = result
    
    return answer