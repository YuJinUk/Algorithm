import sys
from itertools import combinations
input = sys.stdin.readline
l, c = map(int, input().split())
alpha = list(input().split())
alpha.sort()

vowels = [] # 모음
consonants = [] # 자음
for a in alpha:
    if a in ['a','e','i','o','u']:
        vowels.append(a)
    else:
        consonants.append(a)
for i in combinations(alpha, l):
    cnt_v = len([k for k in i if k in vowels])
    cnt_l = l - cnt_v
    if cnt_v > 0 and cnt_l > 1:
        print(''.join(i))