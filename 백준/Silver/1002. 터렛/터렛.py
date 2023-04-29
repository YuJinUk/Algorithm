import sys, math
input = sys.stdin.readline

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if not distance and r1 == r2:
        print(-1)
    elif distance > r1 + r2:
        print(0)
    elif distance == r1 + r2 or distance == abs(r1-r2):
        print(1)
    elif distance < r1 + r2 and distance > abs(r1 - r2):
        print(2)
    else:
        print(0)