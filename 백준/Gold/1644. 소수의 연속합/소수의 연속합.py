def sosu(x):
    table = [False] * (x+1)
    table[0] = True
    table[1] = True
    for i in range(2, x+1):
        for j in range(i*2, x+1, i):
            table[j] = True
    return table

import sys
input = sys.stdin.readline
n = int(input())
if n == 1:
    print(0)
    exit()
table = sosu(n)
num = []
for idx, i in enumerate(table):
    if not i:
        num.append(idx)
i, j, cnt = 0, 1, 0
check = num[i]
# print(num)
while i < len(num):
    if check > n:
        check -= num[i]
        i += 1
        continue
    if check == n:
        cnt += 1
    if i == len(num)-1:
        break
    # print(j)
    check += num[j]
    j += 1
    if j == len(num):
        check -= num[i]
        i += 1
        j = i + 1
print(cnt)