import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

S = list(input().rstrip())
T = list(input().rstrip())

def f(start, end):
    if len(start) == len(end):
        if ''.join(start) == ''.join(end):
            print(1)
            sys.exit(0)
    if len(start) < len(end):
        if end[-1] == 'A':
            f(start, end[:len(end)-1])
        if end[0] == 'B':
            f(start, end[::-1][:len(end)-1])
f(S, T)
print(0)