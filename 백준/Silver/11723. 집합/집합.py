import sys
input = sys.stdin.readline
n = int(input())
s = [0] * 21
def f(x, y):
    global s
    if x == 'add':
        s[y] = 1
    elif x == 'check':
        print(s[y])
    elif x == 'remove':
        s[y] = 0
    elif x == 'toggle':
        if s[y]:
            s[y] = 0
        else:
            s[y] = 1
    elif x == 'all':
        for i in range(1, 21):
            s[i] = 1
    elif x == 'empty':
        for i in range(1, 21):
            s[i] = 0
for _ in range(n):
    x = list(input().split())
    if len(x) == 2:
        f(x[0], int(x[1]))
    else:
        f(x[0], 0)