from collections import deque

def solution(maps):

    row = len(maps)-1
    column = len(maps[0])-1
    dxdy = [(-1,0),(1,0),(0,-1),(0,1)]

    graph = [[-1 for _ in range(column+1)] for _ in range(row+1)]

    visited = deque()
    visited.append((0, 0))

    graph[0][0] = 1

    while visited:
        x, y = visited.popleft()
        for dx, dy in dxdy:
            nx = x + dx
            ny = y + dy

            if 0 <= nx <= row and 0 <= ny <= column and maps[nx][ny] == 1 and (nx, ny) not in visited:
                if graph[nx][ny] == -1:
                    graph[nx][ny] = graph[x][y] + 1
                    visited.append((nx, ny))

    return graph[row][column]