import sys
from math import log2
input = sys.stdin.readline

def sum_f(x):
    if x <= 0:
        return 0
    n = int(log2(x))  # 2**n <= x <= 2**(n+1)
    x_log2 = 2 ** n
    if x_log2 == x:
        return n * x // 2 + 1 # Sigma(k = 0 ~ n) k * nCk == n * 2**(n-1) + 1 
    diff = x - x_log2 # x - x_log2 : 맨 앞의 1의 개수
    return n * x_log2 // 2 + 1 + diff + sum_f(diff)

a, b = map(int, input().split())
print(sum_f(b) - sum_f(a - 1)) # b까지의 1의 개수 - (a-1)까지의 1의 개수