n, k, m = map(int, input().split())
node = [list(map(int, input().split())) for _ in range(m)]

for i, j in node:
    a, b = min(i,j), max(i,j)
    if k == 1:
        print(b-a)
        continue
    cnt = 0
    while True:
        b = (b-2)//k + 1
        if a == b:
            break
        elif a > b:
            a, b = b, a
        cnt += 1
    print(cnt+1)