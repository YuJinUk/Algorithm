import sys
input = sys.stdin.readline
def sosu(n):
    table = [False] * (n+1)
    table[0] = True
    table[1] = True
    for i in range(2, int(n**0.5)+1):
        for j in range(i*2, n+1, i):
            table[j] = True
    return table
n = int(input())
table = sosu(n)
for idx, i in enumerate(table):
    if not i:
        while not n % idx:
            n //= idx
            print(idx)
    if n == 1:
        break