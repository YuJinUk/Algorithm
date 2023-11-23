from collections import deque

def dfs(place):
    dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    place = "".join(place)
    for idx, p in enumerate(place):
        queue = deque()
        visited = deque()
        if p == "P":
            rx, ry = divmod(idx, 5)
            queue.append((rx, ry, 0))
            visited.append((rx, ry))
            flag = 0
            while queue:
                cx, cy, cnt = queue.pop()
                if cnt == 2:
                    continue
                for dx, dy in dxdy:
                    nx, ny = cx + dx, cy + dy
                    if -1 < nx < 5 and -1 < ny < 5 and (nx, ny) not in visited and place[nx * 5 + ny] != "X":
                        if place[nx * 5 + ny] == "P":
                            return False
                        queue.append((nx, ny, cnt + 1))
                        visited.append((nx, ny))
    return True

def solution(places):
    answer = []
    for p in places:
        if dfs(p):
            answer.append(1)
        else:
            answer.append(0)    
    return answer