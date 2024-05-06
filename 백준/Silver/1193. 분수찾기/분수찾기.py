import sys

input = sys.stdin.readline

N = int(input().rstrip())

def f(x):
    return 1 + (x + 1) * x // 2 - x

n, result = 0, 0

while True:
    n += 1
    left, right = f(n), f(n + 1)
    if left == N:
        break
    elif left < N < right:
        result = N - left
        break

fraction_even = [str(1 + result), '/', str(n - result)]
fraction_odd = [str(n - result), '/', str(1 + result)]

if n % 2:
    print(''.join(fraction_odd))
else:
    print(''.join(fraction_even))