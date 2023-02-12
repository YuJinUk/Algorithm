for tt in range(1, 11):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    x = len(data)-1
    y_list = []
    for idx, i in enumerate(data[x]):
        if i == 1:
            y_list.append(idx)
    cnt_list =[]
    result = []
    for y in y_list:
        cnt = 0
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
            cnt += 1
            if x == 0:
                cnt_list.append(cnt)
                result.append(y)
                x = len(data)-1
                break
    print(f'#{tt} {result[cnt_list.index(min(cnt_list))]}')