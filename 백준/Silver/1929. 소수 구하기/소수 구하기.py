def sosu(n):
    table = [True] * (n + 1)
    table[0] = False
    table[1] = False
    if n == 1:
        return False
    for i in range(2, n+1):
        for j in range(i*2, n+1, i):
            table[j] = False
    return table

import sys
input = sys.stdin.readline
start, end = map(int, input().split())
answer = sosu(end)
for i in range(start, end+1):
    if answer[i]:
        print(i)