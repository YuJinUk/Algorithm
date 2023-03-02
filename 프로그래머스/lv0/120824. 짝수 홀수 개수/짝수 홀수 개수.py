def solution(num_list):
    return [sum([1 for num in num_list if not num%2]) ,sum([1 for num in num_list if num%2])]