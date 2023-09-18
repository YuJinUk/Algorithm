import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
A = sorted(list(map(int, input().split())), reverse = True)
B = sorted(list(map(int, input().split())))

answer = 0
for idx in range(N):
    answer += A[idx] * B[idx]
print(answer)