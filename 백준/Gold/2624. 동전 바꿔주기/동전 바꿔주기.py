def solution(n, money):
    check = [0] * (n+1)
    check[0] = 1
    money.sort()
    l = len(money)
    for j in money:
        m, cnt = j
        for i in range(n, -1, -1):
            for k in range(1, cnt+1):
                if i - m*k >= 0:
                    check[i] += check[i-m*k]
    print(check[-1])

t = int(input())
k = int(input())
money = [tuple(map(int, input().split())) for _ in range(k)]
money.sort()
solution(t, money)