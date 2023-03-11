def solution(num_list, n):
    return [[num_list[j] for j in range(i*n,(i+1)*n)] for i in range(len(num_list)//n)]