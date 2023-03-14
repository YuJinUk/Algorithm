s, p = map(int, input().split())
if s>p:
    print(2)
    exit()
for i in range(1, s+1):
    if (s/i)**i >= p:
        print(i)
        break
else:
    print(-1)