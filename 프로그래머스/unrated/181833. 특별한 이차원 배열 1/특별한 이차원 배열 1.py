def solution(n):
    return [[1 if idx == jdx else 0 for jdx, j in enumerate(range(n))] for idx, i in enumerate(range(n))]