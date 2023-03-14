import sys
def extended_gcd(a, b):
    check, x0, x1, y0, y1 = a, 1, 0, 0, 1
    while b:
        q, r = divmod(a, b)
        a, b = b, r
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    if y0 < 0:
        y0 += check
    if a != 1 or y0 > 1e9:
        return 'IMPOSSIBLE'
    return y0
T = int(sys.stdin.readline().rstrip())
for tt in range(1, T+1):
    k, c = map(int, sys.stdin.readline().rstrip().split())
    if c == 1:
        if k>=1e9:
            print('IMPOSSIBLE')
            continue
        else:
            print(k+1)
            continue
    if k == 1:
        print(1)
        continue
    print(extended_gcd(k, c))