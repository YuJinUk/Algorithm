import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())

gap, remain = a-b, v-a
mok, mod = divmod(remain, gap)
if mod :
    answer = mok + 2
else:
    answer = mok + 1
print(answer)