import sys
input = sys.stdin.readline

S = int(input())

answer = 0
i = 1
while True:
    S -= i
    answer += 1
    if S < 0:
        answer -= 1
        break
    elif not S:
        break
    i += 1
print(answer)