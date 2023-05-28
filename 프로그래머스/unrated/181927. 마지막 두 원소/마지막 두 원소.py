def solution(num_list):
    check = num_list[-1] - num_list[-2]
    if check > 0: num_list.append(check)
    else : num_list.append(num_list[-1]*2)
    return num_list