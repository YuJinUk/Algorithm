import sys

input = sys.stdin.readline

String = input().rstrip()
N = int(input().rstrip())

print(String[N-1])