import sys

input = sys.stdin.readline

N = int(input().rstrip())

for idx in range(N):
    x, y = map(int, input().split())
    print(f"Case #{idx + 1}: {x + y}")