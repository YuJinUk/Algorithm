T = int(input())
for tt in range(1, T+1):
    n = int(input())
    coin = [50000,10000,5000,1000,500,100,50,10]
    result = []
    for c in coin:
        mok, mod = divmod(n, c)
        result.append(mok)
        n = mod
    print(f'#{tt}')
    print(*result)