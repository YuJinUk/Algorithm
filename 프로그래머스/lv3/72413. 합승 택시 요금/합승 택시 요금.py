def solution(n, s, a, b, fares):
    answer = float('inf')
    
    dic = dict()
    for i in range(1, n+1):
        dic[i] = dict()
        for j in range(1, n+1):
            dic[i][j] = float('inf')
        dic[i][i] = 0
        
    for i, j, k in fares:
        dic[i][j] = k
        dic[j][i] = k
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                dic[i][j] = min(dic[i][j], dic[i][k] + dic[k][j])

    for i in range(1,n+1):
        cost = dic[s][i] + dic[i][a] + dic[i][b]
        answer = min(answer,cost)
    return answer