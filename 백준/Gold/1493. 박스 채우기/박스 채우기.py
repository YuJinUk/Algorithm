from sys import stdin
l, w, h = map(int, stdin.readline().split())
n = int(stdin.readline())
cube = [tuple(map(int, stdin.readline().split())) for _ in range(n)]
cube.sort(reverse=True)

v = l*w*h
cnt = 0
check = 0
answer = 0
for s, c in cube:
    s = 1 << s
    # print('sss', s)
    cnt *= 8
    pos = (l//s) * (w//s) * (h//s) - cnt
    min_value = min(pos, c)
    check += min_value * (s**3)
    cnt += min_value
    answer += min_value
    # print(pos, cnt)
    # print('check',check)
if check == v:
    print(answer)
else:
    print(-1)