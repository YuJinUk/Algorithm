import sys
n, b, c = map(int,sys.stdin.readline().split())
ramen = list(map(int, sys.stdin.readline().rstrip().split())) + [0] * 2
answer = 0
if b < c:
    answer += sum(ramen) * b
    print(answer)
    exit()
for i in range(len(ramen)):
    if ramen[i] and ramen[i+1] and ramen[i+2]:
        if ramen[i+1] > ramen[i+2]: # 2개씩 2번이 3개 1번 1개 1번보다 더 쌈
            min_ramen = min(ramen[i], ramen[i+1]-ramen[i+2])
            ramen[i] -= min_ramen
            ramen[i+1] -= min_ramen
            answer += min_ramen * (b+c)
        min_ramen = min(ramen[i], ramen[i+1], ramen[i+2])
        ramen[i] -= min_ramen
        ramen[i+1] -= min_ramen
        ramen[i+2] -= min_ramen
        answer += min_ramen * (b+2*c)
    elif ramen[i] and ramen[i+1] and not ramen[i+2]:
        min_ramen = min(ramen[i], ramen[i+1])
        ramen[i] -= min_ramen
        ramen[i+1] -= min_ramen
        answer += min_ramen * (b+c)
    answer += ramen[i] * b
    ramen[i] = 0
print(answer)