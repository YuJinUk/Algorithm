def solution(sides):
    return 1 if sorted(sides)[-1] < sorted(sides)[-2] + sorted(sides)[-3] else 2