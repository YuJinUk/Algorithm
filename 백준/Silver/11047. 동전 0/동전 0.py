import sys

input = sys.stdin.readline

N, K = map(int, input().split())

coin = []

for _ in range(N):
    x = int(input())
    if x > K:
        continue
    coin.append(x)

answer = 0
while coin:
    x = coin.pop()
    mok, mod = divmod(K, x)
    answer += mok
    K = mod

print(answer)