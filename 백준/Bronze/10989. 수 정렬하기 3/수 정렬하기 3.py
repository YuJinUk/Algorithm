import sys
n = int(sys.stdin.readline())
# max_num = 10000
lst = [0] * 10001
for _ in range(n):
    lst[int(sys.stdin.readline())] += 1
for i in range(1, 10001):
    for _ in range(lst[i]):
        print(i)