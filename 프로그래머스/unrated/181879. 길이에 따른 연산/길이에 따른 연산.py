def solution(num_list):
    x = 1
    for i in num_list:
        x *= i
    return sum(num_list) if len(num_list) > 10 else x