import sys
input = sys.stdin.readline
h, m = map(int, input().split())
x = int(input())
mok, mod = divmod(m+x, 60)
mok2, mod2 = divmod(h+mok, 24)
print(mod2, mod)