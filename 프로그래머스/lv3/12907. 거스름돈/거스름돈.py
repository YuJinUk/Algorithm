def solution(n, money):
    check = [0] * (n+1)
    check[0] = 1
    money.sort()
    l = len(money)
    for j in money:
        for i in range(n+1):
            if i >= j:
                check[i] += check[i-j]
    return check[-1] % (10**9 + 7)