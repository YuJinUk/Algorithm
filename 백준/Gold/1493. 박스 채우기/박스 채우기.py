from sys import stdin
l, w, h = map(int, stdin.readline().split())
n = int(stdin.readline())
cube = [tuple(map(int, stdin.readline().split())) for _ in range(n)]
cube.sort(reverse=True)

v = l*w*h # 총 넓이
cnt = 0 # 정육각형 사이즈 별 부피에 따라 제거해줘야하는 상자의 개수
check = 0 # 최종 넓이
answer = 0 # 정육각형 개수
for s, c in cube:
    s = 1 << s
    cnt *= 8
    pos = (l//s) * (w//s) * (h//s) - cnt
    min_value = pos if pos < c else c
    check += min_value * (s**3)
    cnt += min_value
    answer += min_value
if check == v:
    print(answer)
else:
    print(-1)