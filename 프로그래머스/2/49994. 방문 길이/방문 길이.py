from collections import deque
def solution(dirs):
    dirs = deque(list(dirs))
    start = [0,0]
    visited = deque()
    while len(dirs):
        d = dirs.popleft()
        end = start.copy()
        if d == 'U' and start[1] < 5:
            end[1] += 1
        elif d == 'D' and start[1] > -5:
            end[1] -= 1
        elif d == 'R' and start[0] < 5:
            end[0] += 1
        elif d == 'L' and start[0] > -5:
            end[0] -= 1
        else:
            continue
        if [start]+[end] not in visited and [end]+[start] not in visited:
            visited.append([start]+[end])
        start = end.copy()

    return len(visited)