import sys
from math import gcd
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    gcd_ = gcd(a, b)
    print(a * b // gcd_)