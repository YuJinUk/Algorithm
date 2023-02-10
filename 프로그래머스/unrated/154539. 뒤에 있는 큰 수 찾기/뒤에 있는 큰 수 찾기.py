from collections import deque
def solution(numbers):
    if sorted(numbers, reverse=True) == numbers or len(set(numbers)) == 1:
        return [-1]*len(numbers)
    result = [-1] * len(numbers)
    mod = deque()
    for idx, num in enumerate(numbers):
        while mod and numbers[mod[-1]] < num:
            result[mod[-1]] = num
            mod.pop()
        mod.append(idx)
    return result