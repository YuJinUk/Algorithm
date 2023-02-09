T = int(input())
for tt in range(1,T+1):
    cnt = 0
    first, second= input().split()
    i = 0
    while i < len(first):
        if first[i] == second[0] and first[i:i+len(second)] == second:
            i += len(second)
            cnt += 1
        else:
            i += 1
            cnt += 1
    print(f'#{tt} {cnt}')