import sys
n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
answer = 0
max_v = max(lst)
for i in lst:
    answer += 100 * i / max_v
print(round(answer/n, 2))