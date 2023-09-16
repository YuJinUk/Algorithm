import sys
input = sys.stdin.readline

k, d, a = map(int, input().rstrip().split('/'))
if k + a < d or not d: print('hasu')
else: print('gosu')