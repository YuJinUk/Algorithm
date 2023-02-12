for tt in range(1, 11):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    x = len(data)-1
    y = data[x].index(2)
    dxdy = [(0, 1),(0, -1),(-1,0)] # 동 서 북
    visited = [(x,y)]
    while True:
        for dx, dy in dxdy:
            x = x + dx
            y = y + dy 
            if 0<=x and 0<=y<=99 and data[x][y] and (x,y) not in visited:
                visited.append((x,y))
                break
            else:
                x -= dx
                y -= dy
        if x == 0:
            break    
    print(f'#{tt} {y}')