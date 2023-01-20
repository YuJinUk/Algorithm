def solution(x):
    for i in range(1,len(x)):
        for idx in range(4):
            sum_num = max(x[i-1][:idx] + x[i-1][idx+1:])
            x[i][idx] += sum_num 
    return max(x[-1])