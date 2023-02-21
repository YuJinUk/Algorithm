def solution(maps):
    map = [list(i) for i in maps]
    row = len(map)
    column = len(map[0])
    island = [(i,j) for i in range(row) for j in range(column) if map[i][j] != 'X']
    dxdy = [(1,0),(-1,0),(0,1),(0,-1)]
    visited = []
    result = set()
    ans = []
    for i,j in island:
        if (i,j) not in result:
            visited.append((i,j))
            cnt = 0
            while visited:
                x, y = visited.pop()
                for dx, dy in dxdy:
                    nx = x + dx
                    ny = y + dy
                    # print(x, y, nx, ny)
                    if -1 < nx < row and -1 < ny < column and (nx,ny) not in result and map[nx][ny] != 'X':
                        visited.append((nx, ny))
                        result.add((nx, ny))
                        cnt += int(map[nx][ny])
            if not cnt:
                cnt += int(map[x][y])
            ans.append(cnt)
    if not ans:
        return [-1]
    return sorted(ans)