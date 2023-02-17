def solution(p): # p : prices

    p = p+[0]
    l = len(p) 
    result = []
    i = 0
    while i < l-2:
        for j in range(i+1, l): 
            if p[i] > p[j] or j == l-2:
                result.append(j-i)
                break
        i += 1          
    
    return result + [0]