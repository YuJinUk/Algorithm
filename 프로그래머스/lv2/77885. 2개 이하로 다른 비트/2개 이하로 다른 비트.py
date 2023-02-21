def solution(li):
    
    result = []
    
    for i in li:
        if i % 2 == 0:
            result.append(i+1)
            continue
            
        else:
            x = '0' + bin(i)[2:]
            idx = x.rfind('0')
            x = list(x)
            x[idx] = '1'
            x[idx+1] = '0'
            result.append(int(''.join(x), 2))
    return result