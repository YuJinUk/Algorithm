def solution(num_list):
    answer = 1
    for i in num_list:
        answer = answer * i
    return 1 if sum(num_list)**2 > answer else 0