T = int(input())
for tt in range(1,T+1):
    n = int(input())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            x, y = 0, 0
            a, b = i, j
            start = (a,b)
            if matrix[a][b]:
                while b<n-1:
                    b += 1
                    y += 1
                    if not matrix[a][b]:
                        b -= 1
                        break
                while a<n-1:
                    a += 1
                    x += 1
                    if not matrix[a][b]:
                        a -= 1
                        break
                result.append((x,y,(x)*(y)))
            for xx in range(start[0], start[0]+x):
                for yy in range(start[1], start[1]+y):
                    matrix[xx][yy] = 0
    result.sort(key = lambda x : (x[2], x[0]))
    print(f'#{tt} {len(result)}', end= ' ')
    for i in result:
        print(i[0],i[1], end = ' ')
    print()