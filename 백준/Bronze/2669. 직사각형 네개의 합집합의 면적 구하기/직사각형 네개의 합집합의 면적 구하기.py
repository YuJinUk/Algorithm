n = [list(map(int, input().split())) for _ in range(4)]
new = list(set([(j, k) for x1,y1,x2,y2 in n for j in range(x1,x2) for k in range(y1, y2)]))
print(len(new))