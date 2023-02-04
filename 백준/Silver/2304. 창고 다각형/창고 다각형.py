def sol(N, n):

    if N == 1:
        return n[0][1]

    n.sort()
    max_n = max(n, key = lambda x: (x[1], x[0]))
    max_idx = n.index(max_n)
    sum_area = 0

    i = 0
    j = 1
    while i < max_idx and j< max_idx+1:
        if n[i][1] < n[j][1]:
            sum_area += n[i][1] * (n[j][0]- n[i][0])
            i = j
            j += 1
        else :
            j += 1
        if j == max_idx:
            sum_area += n[i][1] * (max_n[0]- n[i][0])
            break
    
    i = N - 1
    j = N - 2
    while i > max_idx and j > max_idx-1:
        if n[i][1] < n[j][1]:
            sum_area += n[i][1] * (n[i][0]- n[j][0])
            i = j
            j -= 1
        else:
            j -= 1
        if j == max_idx-1 :
            sum_area += n[i][1] * (n[i][0]- max_n[0])
            break
            
    return sum_area + max_n[1]

a = int(input()) # 1<= N <=1000
b = [tuple(map(int,input().split())) for _ in range(a)] # (a,b) a : location, b : height

print(sol(a, b))