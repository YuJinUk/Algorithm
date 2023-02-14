T = int(input())
for tt in range(1,T+1):
    n, k = map(int, input().split())
    num = list(map(int, input().split()))
    result = []
    for i in range(1,n+1):
        if i not in num:
            result.append(i)
    print(f'#{tt}', *result)