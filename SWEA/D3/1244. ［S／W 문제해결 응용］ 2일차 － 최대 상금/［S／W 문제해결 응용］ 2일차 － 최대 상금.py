T = int(input())
for tt in range(1, T+1):
    n, cnt = input().split()
    n, cnt = list(n), int(cnt)
    if len(n) == 2:
        if cnt % 2:
            n = reversed(n)
        print(f"#{tt} {''.join(n)}")
        continue
    if not cnt:
        print(f"#{tt} {''.join(n)}")
        continue
    sort_n = sorted(n, reverse=True)
    dn = 0
    if len(set(n)) < len(n):
            dn = 1
    if n == sort_n:
        if dn or not cnt % 2:
            print(f"#{tt} {''.join(n)}")
        elif cnt % 2:
            n[-1], n[-2] = n[-2], n[-1]
            print(f"#{tt} {''.join(n)}")
        continue
    ans = set()
    check = dict()
    # print(check)
    def rec(lst, count):
        global cnt
        if tuple(lst) in check:
            return 0
        if count == cnt:
            return int(''.join(lst))
        if lst == sort_n:
            return 0
        check[tuple(lst)] = 1
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                lst[i], lst[j] = lst[j], lst[i]
                ans.add(rec(lst, count+1))
                lst[i], lst[j] = lst[j], lst[i]
        return 0
    rec(n, 0)
    # print(check)
    # print(ans)
    print(f'#{tt} {max(ans)}')