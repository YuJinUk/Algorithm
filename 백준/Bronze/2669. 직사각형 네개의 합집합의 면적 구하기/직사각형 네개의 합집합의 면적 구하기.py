n = [list(map(int, input().split())) for _ in range(4)]
new = []
for i in n:
    x1, y1, x2, y2 = i[0],i[1],i[2],i[3]
    new += [[j, k] for j in range(x1,x2) for k in range(y1, y2) if [j,k] not in new]
print(len(new))