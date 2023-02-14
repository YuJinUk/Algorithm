T = int(input())
for tt in range(1, T+1):
    n = int(input())
    num = list(map(int, input().split()))
    result = []
    for i in range(n-1):
        for j in range(i+1, n):
            result.append(num[i] * num[j])
    ans = []
    for k in result:
        k = str(k)
        for h in range(len(k)-1):
            if k[h]>k[h+1]:
                break
        else:
            ans.append(int(k))
    if not ans:
        print(f'#{tt} -1')
        continue
    print(f'#{tt} {max(ans)}')