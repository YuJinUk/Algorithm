import sys

input = sys.stdin.readline

x, y, z = map(int, input().split())

check = [0] * (x + y + z + 1)

for i in range(1, x + 1):
    for j in range(1, y + 1):
        for k in range(1, z + 1):
            check[i + j + k] += 1

print(check.index(max(check)))