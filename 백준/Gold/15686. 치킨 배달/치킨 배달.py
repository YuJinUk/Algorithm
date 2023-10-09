import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())

matrix, chick, house = [], [], []
for row_idx in range(N):
    row = list(map(int, input().split()))
    for col_idx, col in enumerate(row):
        if col == 1: house.append((row_idx, col_idx))
        elif col == 2: chick.append((row_idx, col_idx))
    matrix.append(row)


def f(chicken, myhome):
    global answer
    result = 0
    for mx, my in myhome:
        check = int(1e9)
        for cx, cy in chicken:
            checking = abs(cx - mx) + abs(cy - my)
            if check > checking: check = checking
        result += check
        if result >= answer:
            return answer
    return result

answer = int(1e9)
for choose in list(combinations(chick, M)):
    answer = f(choose, house)
print(answer)