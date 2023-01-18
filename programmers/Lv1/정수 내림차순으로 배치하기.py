def solution(n):
    reverselist = sorted(str(n), reverse = True)
    return int("".join(reverselist))