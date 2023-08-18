import sys
input = sys.stdin.readline

n = int(input().rstrip())

if not n // 10:
    n *= 10

answer = 0
check = n
while True:
    mok, mod = divmod(n, 10)
    n = (n%10)*10 + (mok+mod)%10
    answer += 1
    if check == n:
        break
print(answer)