n, m = map(int, input().split())

visit = [False] * (m-n+1)
cnt = 0
i = 2
while i**2 <= m:
    mok, mod = divmod(n, i**2)
    if not mod:
        while (i**2)*mok <= m:
            if not visit[(i**2) * mok - n]:
                visit[(i**2) * mok - n] = True
                cnt += 1
            mok += 1
    elif mod:
        while (i**2) * (mok+1) <= m:
            if not visit[(i**2) * (mok+1) - n]:
                visit[(i**2) * (mok+1) - n] = True
                cnt += 1
            mok += 1
    i += 1
print(m - n + 1 - cnt)