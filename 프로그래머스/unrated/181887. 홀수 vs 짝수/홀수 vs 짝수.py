def solution(num_list):
    odds = sum([num_list[i] for i in range(0, len(num_list), 2)])
    evens = sum(num_list) - odds
    return odds if odds > evens else evens