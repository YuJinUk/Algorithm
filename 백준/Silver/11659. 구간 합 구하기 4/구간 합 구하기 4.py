import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

matrix = []

accumulate = 0
for i in nums:
    accumulate += i
    matrix.append(accumulate)
    
for _ in range(m):
    s, e = map(int, input().split())
    if s > 1: print(matrix[e-1] - matrix[s-2])
    else: print(matrix[e-1])