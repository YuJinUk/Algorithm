import sys
n = int(sys.stdin.readline())
ramen = list(map(int, sys.stdin.readline().rstrip().split())) + [0] * 2
answer = 0
for i in range(len(ramen)):
    if ramen[i] and ramen[i+1] and ramen[i+2]:
        if ramen[i+1] > ramen[i+2]: # 2개씩 2번이 3개 1번 1개 1번보다 더 쌈
            min_ramen = min(ramen[i], ramen[i+1]-ramen[i+2])
            ramen[i] -= min_ramen
            ramen[i+1] -= min_ramen
            answer += min_ramen * 5
        min_ramen = min(ramen[i], ramen[i+1], ramen[i+2])
        ramen[i] -= min_ramen
        ramen[i+1] -= min_ramen
        ramen[i+2] -= min_ramen
        answer += min_ramen * 7
    elif ramen[i] and ramen[i+1] and not ramen[i+2]:
        min_ramen = min(ramen[i], ramen[i+1])
        ramen[i] -= min_ramen
        ramen[i+1] -= min_ramen
        answer += min_ramen * 5
    answer += ramen[i] * 3
    ramen[i] = 0
print(answer)